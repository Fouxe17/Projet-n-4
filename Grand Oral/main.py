from p5 import *

import classes.bullets as bullets

import updaters.fps as fps

W,H = 750,500
MW,MH = W/2,H/2
BACKGROUND_COLOR = 128
TURRET_COLOR = (255,0,4)

state = "Without pooling"
previous_clicking_state = False
current_clicking_state = False
clicking = False
angle = 0

def getMousePosition():
    return mouse_x,mouse_y #type:ignore

def updateMouseClickingState():
    global current_clicking_state, clicking, previous_clicking_state
    current_clicking_state = mouse_is_pressed #type:ignore
    clicking = previous_clicking_state != current_clicking_state and current_clicking_state
    previous_clicking_state = current_clicking_state

def drawTurret():
    global angle
    #Canon de la tourelle
    mouse_x,mouse_y = getMousePosition()

    X = MW - mouse_x
    Y = MH - mouse_y

    angle = atan2(Y,X)

    translate(MW,MH)
    rotate(angle)

    noStroke()
    fill(0)
    
    rectMode(CENTER)
    rect(-15,0,50,20)

    fill(*TURRET_COLOR)
    ellipse(0,0,30,30)

def updateEvents():
    if clicking:
        bullets.AddBullet(angle)
    fps.update()

def mainUI():
    reset_matrix()
    background(BACKGROUND_COLOR)

    fill(0,255,0)
    rect(W - 125 - 30, H- 75, 50, 50)
    fill(255,0,0)
    rect(W - 75, H- 75, 50, 50)

def setup():
    size(W,H)
    background(BACKGROUND_COLOR)

def draw():
    updateMouseClickingState()
    updateEvents()

    mainUI()

    bullets.updateBullets()
    reset_matrix()
    drawTurret()

run()