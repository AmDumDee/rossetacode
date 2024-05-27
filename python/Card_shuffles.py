import random

def riffleShuffle(va, flips):
    nl = va
    for n in range(flips):
        
        cutPoint = len(nl)/2 + random.choice([-1, 1]) * random.randint(0, len(va)/10)

        
        left = nl[0:cutPoint]
        right = nl[cutPoint:]

        del nl[:]
        while (len(left) > 0 and len(right) > 0):
            
            if (random.uniform(0, 1) >= len(left) / len(right) / 2):
                nl.append(right.pop(0))
            else:
                nl.append(left.pop(0))
        if (len(left) > 0):
            nl = nl + left
        if (len(right) > 0):
            nl = nl + right
    return nl

def overhandShuffle(va, passes):
    mainHand = va
    for n in range(passes):
        otherHand = []
        while (len(mainHand) > 0):
            
            cutSize = random.randint(0, len(va) / 5) + 1
            temp = []

            
            i=0
            while (i<cutSize and len(mainHand) > 0):
                temp.append(mainHand.pop(0))
                i = i + 1

            
            if (random.uniform(0, 1) >= 0.1):
                
                otherHand = temp + otherHand
            else:
                otherHand = otherHand + temp
        
        mainHand = otherHand
    return mainHand

print("Riffle shuffle")
nums = [x+1 for x in range(21)]
print(nums)
print(riffleShuffle(nums, 10))
print

print("Riffle shuffle")
nums = [x+1 for x in range(21)]
print(nums)
print(riffleShuffle(nums, 1))
print

print("Overhand shuffle")
nums = [x+1 for x in range(21)]
print(nums)
print(overhandShuffle(nums, 10))
print

print("Overhand shuffle")
nums = [x+1 for x in range(21)]
print(nums)
print(overhandShuffle(nums, 1))
print

print("Library shuffle")
nums = [x+1 for x in range(21)]
print(nums)
random.shuffle(nums)
print(nums)
print
