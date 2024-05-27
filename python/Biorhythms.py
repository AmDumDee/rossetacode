from datetime import date, timedelta
from math import floor, sin, pi

def biorhythms(birthdate,targetdate):
    
    
    
    print("Born: "+birthdate+" Target: "+targetdate)    
    
    
    
    birthdate = date.fromisoformat(birthdate)
    targetdate = date.fromisoformat(targetdate)
    
    
    
    days = (targetdate - birthdate).days
    
    print("Day: "+str(days))
    
    
    
    cycle_labels = ["Physical", "Emotional", "Mental"]
    cycle_lengths = [23, 28, 33]
    quadrants = [("up and rising", "peak"), ("up but falling", "transition"),
                   ("down and falling", "valley"), ("down but rising", "transition")]
    
    for i in range(3):
        label = cycle_labels[i]
        length = cycle_lengths[i]
        position = days % length
        quadrant = int(floor((4 * position) / length))
        percentage = int(round(100 * sin(2 * pi * position / length),0))
        transition_date = targetdate + timedelta(days=floor((quadrant + 1)/4 * length) - position)
        trend, next = quadrants[quadrant]
        
        if percentage > 95:
            description = "peak"
        elif percentage < -95:
             description = "valley"
        elif abs(percentage) < 5:
             description = "critical transition"
        else:
             description = str(percentage)+"% ("+trend+", next "+next+" "+str(transition_date)+")"
        print(label+" day "+str(position)+": "+description)
    
    
biorhythms("1943-03-09","1972-07-11")
