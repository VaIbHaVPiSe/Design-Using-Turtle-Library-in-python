from turtle import *
import turtle as tur
import random
import time

t=tur.Turtle()
tur.title("Vaibhav")
tur.speed(10)

tur.bgcolor("black")
tur.color("red")
tur.pensize(5)

tur.left(60)
tur.fd(50)
tur.left(15)
tur.circle(100,90)
tur.fd(30)
tur .pensize(10)
tur.penup()
tur.right(90)
tur.fd(20)
tur.pendown()

tur.right(40)
tur.circle(-50,90)
tur.fd(20)
tur.left(150)

#seconde head curve
tur.color("red")
tur.penup()
tur.fd(40)
tur.left(20)
tur.pendown()
tur.circle(50,90)

#third head curve

#goto beginning
tur.color("red")
tur.penup()
goto(0,0)
tur.pensize(5)
tur.pendown()
tur.left(30)
tur.fd(120)
tur.circle(60,270)

#eyes
tur.color("silver")
tur.penup()
tur.forward(30)
tur.right(50)
tur.forward(135)
tur.pendown()
tur.pensize(8)
tur.circle(50,90)
tur.left(95)
tur.penup()
tur.circle(60,75)

#eyebrows
tur.penup()
tur.forward(15)
tur.left(90)
tur.pensize(2)
tur.pendown()
tur.circle(70,90)

#ears
tur.pensize(5)
tur.penup()
tur.forward(75)
tur.right(90)
tur.forward(20)
tur.pendown()
tur.circle(90,90)
tur.forward(20)

tur.circle(30,170)
tur.right(180)
tur.circle(28,180)
tur.right(160)
tur.circle(25,180)
tur.right(160)
tur.circle(22,160)
tur.forward(20)
tur.circle(60,45)


#trunk

tur.penup()
goto(0,0)
tur.left(130)
tur.fd(140)
tur.right(250)
tur.backward(20)
tur.circle(80,20)
tur.circle(20,40)

tur.right(110)
tur.penup()
tur.fd(20)
tur.pendown()
tur.pensize(10)
tur.forward(50)
tur.circle(100,80)
tur.pensize(9)
tur.circle(150,50)
tur.pensize(7)
tur.circle(100,60)
tur.pensize(5)
tur.circle(90,60)
tur.pensize(4)
tur.circle(40,60)
tur.circle(10,90)


#head
tur.color("red")
tur.penup()

goto(0,0)

goto(-90,290)
tur.right(230)
tur.pendown()

tur.circle(-100,50)
tur.circle(200,20)
tur.circle(50,30)

tur.right(180)

tur.circle(50,30)
tur.circle(200,20)
tur.circle(-100,40)
tur.right(95)
tur.penup()
tur.fd(40)
tur.right(90)
tur.pendown()
tur.circle(100,40)
tur.penup()
tur.circle(35,120)
tur.right(30)
tur.pendown()
tur.pensize(1)
tur.circle(60,50)

#done
tur.penup()

goto(-70,90)

tur.fillcolor("red")
tur.begin_fill()
tur.circle(20,180)
tur.end_fill()

tur.penup()
tur.left(75)
tur.fillcolor("red")
tur.begin_fill()
tur.circle(70,35)
tur.end_fill()

tur.left(180)
tur.backward(10)
tur.pendown()
tur.left(6)
tur.pensize(5)
tur.color("red")
tur.circle(-80,40)
tur.penup()

goto(0,0)



#borderrrr
tur.write(" ",font=("sans",20,"normal"),align="left")
goto(0,-20)
tur.write(" ",font=("sans",20,"normal"),align="left")

tur.color("orange")
goto(-240,420)
tur.right(90)
tur.pendown()
tur.fillcolor("orange")
tur.begin_fill()
tur.forward(275)
tur.right(130)
tur.forward(100)
tur.end_fill()

tur.penup()
goto(0,420)
tur.right(90)

tur.color("orange")
tur.fillcolor("orange")
tur.begin_fill()
tur.fd(100)
tur.right(50)
tur.pendown()
tur.fd(510)
tur.left(90)
tur.right(165)
tur.end_fill()

tur.color("orange")
tur.fillcolor("orange")
tur.begin_fill()
tur.fd(540)
tur.right(70)
tur.fd(20)
tur.end_fill()

tur.color("orange")
tur.fillcolor("orange")
tur.begin_fill()
tur.fd(540)
tur.right(90)
tur.fd(20)
tur.end_fill()


tur.left(30)
tur.color("orange")
tur.fillcolor("")
tur.begin_fill()
tur.fd(205)
tur.right(90)
tur.fd(20)
tur.end_fill()


tur.color("red")
tur.penup()
goto(0,0)
tur.left(118)
tur.fd(240)
tur.right(30)
tur.pendown()
tur.circle(90,65)
tur.penup()
done()