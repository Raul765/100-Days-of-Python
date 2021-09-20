##Uncoment and run if you need to get new colors
#import colorgram

##relative path to image file
#image_file="Day18 - Intermediate Turtle\Hirst Painting\DAMIEN-HIRST-1992-Ami_6148D_large.jpg"

#colors=colorgram.extract(image_file,30)
#rgb_colors=[]

#for i in colors:
    #r=i.rgb.r
    #g=i.rgb.g
    #b=i.rgb.b
    #new_color=(r,g,b)
    #rgb_colors.append(new_color)

#print(rgb_colors)

painting_colors=[(251, 249, 246), (251, 249, 250), (208, 160, 101), (150, 75, 37), (231, 213, 97), (245, 251, 247), (242, 247, 250), (132, 34, 21), (191, 156, 15), (87, 33, 21), (238, 174, 153), (21, 57, 80), (41, 117, 63), (31, 93, 135), (196, 98, 88), (2, 81, 115), (10, 99, 77), (194, 163, 165), (109, 159, 185), (73, 76, 40), (179, 209, 168), (106, 140, 129), (37, 27, 35), (78, 153, 168), (46, 50, 47), (134, 163, 150), (234, 178, 180), (2, 72, 136), (125, 64, 66), (118, 36, 39)]

import turtle
import random

turtle.colormode(255)
timmy=turtle.Turtle()
timmy.pensize(8)
timmy.speed(0)
timmy.penup()

screen=turtle.Screen()

timmy.sety(-240)
for i in range(9):
    timmy.pencolor(random.choice(painting_colors))
    timmy.setx(-280)
    timmy.dot(50)
    for i in range(9):
        timmy.pencolor(random.choice(painting_colors))
        timmy.fd(61)
        timmy.dot(50)
    timmy.lt(90)
    timmy.fd(61)
    timmy.rt(90)

screen.exitonclick()
