from p5 import *

W,H = 750,500
MW,MH = W/2,H/2

bullets = []

original_settings = {
            "Color": (0,0,0),
            "ExpireTime": .5,
            "Size": (10,10),
            "Speed": 10,
        }

class AddBullet:
    def __init__(self, angle=0, settings={}):
        self.position = [0,0]
        self.settings = original_settings | settings
        self.direction_angle = angle
        self.tick = millis()

        # print(merged_settings)
        bullets.append(self)

    def update(self):
        sets = self.settings

        if millis() - self.tick > sets["ExpireTime"] * 1000:
            return
        
        pos = self.position

        speed = sets["Speed"]

        fill(*sets["Color"])

        # print()
        ellipse(*[*pos, *sets["Size"]])
        
        self.position = [pos[0] - cos(self.direction_angle) * speed, pos[1] - sin(self.direction_angle) * speed]
        

def updateBullets():
    translate(MW,MH)
    for i in bullets:
        i.update()