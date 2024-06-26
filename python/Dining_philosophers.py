import multiprocessing as mp
import random
import time

SCALE = 0.2
THINK = (3, 13)
DINE = (1, 10)

class Philosopher(mp.Process):
    
    def __init__(self, idx, name, run_flag, chopstick_left, chopstick_right,
                 stats, schedule_think, schedule_dine):
        mp.Process.__init__(self)
        self.idx = idx
        self.name = name
        self.run_flag = run_flag
        self.chopstick_left = chopstick_left
        self.chopstick_right = chopstick_right
        self.stats = stats
        self.schedule_think = schedule_think
        self.schedule_dine = schedule_dine
        self.counter = 0
        self.num_dined = 0
        self.hungry_time_total = 0.0
        self.hungry_time_max = 0.0

    def run(self):
        while self.run_flag.value and self.counter < len(self.schedule_think):
        
            time.sleep(self.schedule_think[self.counter]*SCALE)
            duration = -time.perf_counter()
            print(f'{self.name} is hungry', flush=True)
            self.get_chopsticks2()
            duration += time.perf_counter()
            self.hungry_time_total += duration
            self.hungry_time_max = max(self.hungry_time_max, duration)
            self.dining()
        
        self.stats.put({'name': self.name,
                        'num_dined': self.num_dined,
                        'hungry_time_total': self.hungry_time_total,
                        'hungry_time_max': self.hungry_time_max})

    def get_chopsticks(self):
        
        chopstick1, chopstick2 = self.chopstick_left, self.chopstick_right

        while True:
            chopstick1.acquire(True)
            locked = chopstick2.acquire(False)
            if locked:
                return
            chopstick1.release()
            print(f'{self.name} swaps chopsticks', flush=True)
            chopstick1, chopstick2 = chopstick2, chopstick1

    def get_chopsticks0(self):
        
        self.chopstick_left.acquire(True)
        time.sleep(0.1)
        self.chopstick_right.acquire(True)

    def get_chopsticks1(self):
        
        if self.idx == 0:
            chopstick1, chopstick2 = self.chopstick_left, self.chopstick_right
        else:
            chopstick1, chopstick2 = self.chopstick_right, self.chopstick_left
        chopstick1.acquire(True)
        locked = chopstick2.acquire(False)
        if not locked:
            chopstick1.release()
            chopstick2.acquire(True)
            chopstick1.acquire(True)

    def get_chopsticks2(self):
        
        if self.idx == 0:
            chopstick1, chopstick2 = self.chopstick_left, self.chopstick_right
        else:
            chopstick1, chopstick2 = self.chopstick_right, self.chopstick_left
        chopstick1.acquire(True)
        locked = chopstick2.acquire(False)
        if not locked:
            chopstick1.release()
            chopstick2.acquire(True)
            chopstick1.acquire(True)

    def dining(self):
        
        print(f'{self.name} starts eating', flush=True)
        self.num_dined += 1
        time.sleep(self.schedule_dine[self.counter]*SCALE)
        self.counter += 1
        print(f'{self.name} finishes eating and leaves to think.', flush=True)
        self.chopstick_left.release()
        self.chopstick_right.release()

def performance_report(stats):
    
    print("Performance report:")
    for queue in stats:
        data = queue.get()
        print(f"Philosopher {data['name']} dined {data['num_dined']} times. ")
        print(f"  Total wait  : {data['hungry_time_total'] / SCALE}")
        print(f"  Max wait    : {data['hungry_time_max'] / SCALE}")
        if data['num_dined'] > 0:
            print(f"  Average wait: "
                  f"{data['hungry_time_total'] / data['num_dined']/SCALE}")

def generate_philosophers(names, run_flag, chopsticks, stats, max_dine):
    
    num = len(names)
    philosophers = [Philosopher(i, names[i], run_flag,
                                chopsticks[i % num],
                                chopsticks[(i+1) % num],
                                stats[i],
                                [random.uniform(THINK[0], THINK[1])
                                 for j in range(max_dine)],
                                [random.uniform(DINE[0], DINE[1])
                                 for j in range(max_dine)])
                    for i in range(num)]
    return philosophers

def generate_philosophers0(names, run_flag, chopsticks, stats,
                           schedule_think, schedule_dine):
    
    num = len(names)
    philosophers = [Philosopher(i, names[i], run_flag,
                                chopsticks[i % num],
                                chopsticks[(i+1) % num],
                                stats[i],
                                schedule_think[i],
                                schedule_dine[i])
                    for i in range(num)]
    return philosophers

def dining_philosophers(philosopher_names=(('Aristotle', 'Kant',
                                            'Buddha', 'Marx', 'Russel')),
                        num_sec=100, max_dine=100):
    
    num = len(philosopher_names)
    chopsticks = [mp.Lock() for n in range(num)]
    random.seed(507129)
    run_flag = mp.Value('b', True)
    stats = [mp.Queue() for n in range(num)]

    philosophers = generate_philosophers(philosopher_names, run_flag,
                                         chopsticks, stats, max_dine)

    

    for phi in philosophers:
        phi.start()
    time.sleep(num_sec*SCALE)
    run_flag.value = False
    print("Now we're finishing.", flush=True)
    
    wait_time = num*DINE[1]
    while wait_time >= 0 and sum(p.is_alive() for p in philosophers) > 0:
        time.sleep(1)
        wait_time -= 1.0
    if wait_time < 0:
        for phi in philosophers:
            if phi.is_alive():
                print(f"Ooops, {phi.name} has not finished!!")
                phi.terminate()
        return 1
    performance_report(stats)

if __name__ == '__main__':
    dining_philosophers()
