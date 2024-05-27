
from turtle import *
from PIL import Image
import time
import subprocess


colors = ["black", "red", "green", "blue", "magenta", "cyan", "yellow", "white"]

screen = getscreen()


inch_width = 11.0
inch_height = 8.5

pixels_per_inch = 100

pix_width = int(inch_width*pixels_per_inch)
pix_height = int(inch_height*pixels_per_inch)

screen.setup (width=pix_width, height=pix_height, startx=0, starty=0)

screen.screensize(pix_width,pix_height)


left_edge = -screen.window_width()//2

right_edge = screen.window_width()//2

bottom_edge = -screen.window_height()//2

top_edge = screen.window_height()//2


screen.delay(0)
screen.tracer(5)

for inch in range(int(inch_width)-1):
    line_width = inch + 1
    pensize(line_width)
    colornum = 0

    min_x = left_edge + (inch * pixels_per_inch)
    max_x = left_edge + ((inch+1) * pixels_per_inch)
    
    for y in range(bottom_edge,top_edge,line_width):
        penup()
        pencolor(colors[colornum])
        colornum = (colornum + 1) % len(colors)
        setposition(min_x,y)
        pendown()
        setposition(max_x,y)
         
screen.getcanvas().postscript(file="striped.eps")


im = Image.open("striped.eps")
im.save("striped.jpg")


    
subprocess.run(["mspaint", "/pt", "striped.jpg"])
