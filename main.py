import turtle
import random
t = turtle.Turtle()
screen = turtle.Screen()
r = 195
g = 20
b = 50
screen.bgcolor(r,g,b)
t.speed(1000)
t.shape("turtle")
t.color("white")
t.penup()
x = random.randint(-200,200)
y = random.randint(-200,200)
t.goto(x,y)

def turnright():
  t.right(10)
def turnleft():
  t.left(10)
screen.onkey(turnright,"right")
screen.onkey(turnleft,"left")
screen.listen()

dots = []
for i in range(10):
  d = turtle.Turtle()
  d.speed(1000)
  d.color("white")
  d.shape("circle")
  d.penup()
  x = random.randint(-200,200)
  y = random.randint(-200,200)
  d.goto(x,y)
  dots.append(d)
  
def drawstar():
  t.color("yellow")
  t.pendown()
  t.begin_fill()
  for i in range(5):
    t.forward(30)
    t.right(144)
  t.end_fill()
  t.penup()
  t.color("white")
  
stars = 0

while True:
  t.forward(1)
  r-=0.1
  screen.bgcolor(r,g,b)
  if r<30:
    t.write("Game Over!")
    break
  for d in dots:
    if abs(t.xcor()-d.xcor())<10 and abs(t.ycor()-d.ycor())<10:
      drawstar()
      d.goto(1000,1000)
      stars+=1
  if stars==10:
    t.write("I Win")
    break
