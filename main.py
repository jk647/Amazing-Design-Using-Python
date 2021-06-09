# import turtle
import turtle

#make list of color
col =("yellow","red","orange","white","blue","green")

t =turtle.Turtle()
screen =turtle.Screen()
screen.bgcolor("black")
t.speed(30)

for i in range(150):
    t.color(col[i%6])# choose color from col 
    t.forward(i*4)#length of line
    t.left(150)# angle of line
    t.width(4) # width of line