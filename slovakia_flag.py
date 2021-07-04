# Flag of Slovakia

import turtle
t = turtle.Turtle()
t.ht()

def rect(length, width, pencolor, fillcolor):
    before = t.color()
    t.color(pencolor, fillcolor)
    t.begin_fill()
    for i in range(2):
        t.fd(length)
        t.rt(90)
        t.fd(width)
        t.rt(90)
    t.end_fill()
    t.color(*before)

def penup_goto(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()
    
t.speed(0)
    
def draw_crest_background(x, y):
    # (x, y) -> starting pos
    penup_goto(x, y)
    t.color('white', 'white')
    t.begin_fill()
    # Outer curve
    t.rt(90)
    t.fd(100)
    t.circle(90, 70)
    t.setheading(t.heading() + 40)
    t.circle(90, 70)
    t.setheading(90)
    t.fd(100)
    t.lt(90)
    t.fd(10)
    
    #Inner curve
    t.lt(90)
    t.fd(100)
    t.circle(-75, 70)
    t.setheading(t.heading() - 40)
    t.circle(-75, 70)
    t.setheading(90)
    t.fd(100)
    t.goto(x,y)
    t.end_fill()

    #Trace inner curve again, to draw the red section
    #in the crest.
    t.color('black', 'red')
    penup_goto(x + 10, y)
    t.setheading(0)
    t.rt(90)
    t.begin_fill()
    t.fd(100)
    t.circle(75, 70)
    t.setheading(t.heading() + 40)
    t.circle(75, 70)
    t.setheading(90)
    t.fd(100)
    t.goto(x + 10,y)
    t.end_fill()

def draw_flag_background(x, y):
    # (x, y) -> starting pos
    penup_goto(x, y)
    rect(500, 120, 'black', 'white')
    penup_goto(x, y - 120)
    rect(500, 120, 'dark blue', 'dark blue')
    penup_goto(x, y - 240)
    rect(500, 120, 'red', 'red')

def draw_blue_soil():
    #(x1, y1) - left corner, (x2, y2) - right corner
    # angle to draw curve - angle1 for first, angle2 for second
    penup_goto(-220, -50)
    t.pu()
    t.setheading(270)
    t.circle(75, 30)
    x1, y1 = t.position()
    angle1 = t.heading()
    penup_goto(-121, -50)
    t.setheading(270)
    t.circle(-75, 30)
    x2, y2 = t.position()
    angle2 = t.heading()
    t.pd()
    rad = (x2 - x1) / 6

    #Draw the blue portion of the crest.
    t.color('dark blue', 'dark blue')
    t.begin_fill()
    penup_goto(x1, y1)
    t.setheading(90)
    t.circle(-rad+2, 160)
    t.setheading(90)
    t.circle(-rad-4, 180)
    t.setheading(90)
    t.circle(-rad+2, 200)
    t.goto(x2, y2)
    t.setheading(angle2)
    t.circle(-75, 40)
    t.setheading(t.heading() - 40)
    t.circle(-75, 40)
    t.goto(x1, y1)
    t.end_fill()
    
def draw_arm(straight_side_lengths, angle_turn):
    t.fd(straight_side_lengths)
    t.lt(angle_turn)
    t.fd(10)
    t.rt(90 + angle_turn)
    t.fd(20)
    t.rt(90 + angle_turn)
    t.fd(10)
    t.lt(angle_turn)
    t.fd(straight_side_lengths)
    
def draw_white_cross():
    bottom_mid = (-171.17,-68.54)
    t.color('white', 'white')
    penup_goto(bottom_mid[0] - 5, bottom_mid[1])
    t.setheading(90)
    t.begin_fill()
    t.fd(30)
    t.lt(90)
    # bottom left arm
    draw_arm(20, 20)
    t.lt(90)
    t.fd(30)
    for i in range(3):
        # Top, top right and top left arms.
        t.lt(90)
        draw_arm(15, 20)
    t.lt(90)
    t.fd(30)
    t.lt(90)
    #bottom right arm
    draw_arm(20, 20)
    t.lt(90)
    t.fd(30)
    t.rt(90)
    t.fd(10)
    t.end_fill()
    
draw_flag_background(-300, 140)    
draw_crest_background(-230, 50)
draw_white_cross()
draw_blue_soil()
