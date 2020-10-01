#!/usr/bin/env python3

import level1
from time import sleep


class CarBehavior:
    def __init__(self, ti):
        self.target_intesity = ti    
        self.factor = 1
        self.cc = level1.CarControl()
        
         

    def lineFollow(self, speed):
         #Scaling down the intensity, expected range: 2 - 22 - 34   (range of 20 for black, range of 12 for white)
        intensity = self.cc.read_line_sensor()
        if intensity > self.target_intesity:
            speed_correction = round((self.target_intesity-intensity)*self.factor)
            self.cc.drive(speed + speed_correction, speed - speed_correction)
        else:
            speed_correction = round(((self.target_intesity - intensity)/2)*self.factor)
            self.cc.drive(speed + speed_correction, speed - speed_correction)

    
    def cros_line_state(self):
        white = False
        white_counter = 0
        while white == False:
            self.cc.drive(70, 70)
            if self.cc.read_line_counter() > 30:
                white_counter += 1
            if white_counter > 5:
                white = True

    #Kan være der skal tilføjes så vi kigger på eksempelvis de sidste 5-10 værdier fra line counter sensor
    #før vi registrerer det som en linje (Hvis værdien nu ved en fejl jumper ned til sort)
    def straigt(self, lines):
        while lines > 0:
            self.lineFollow(70)
            if self.cc.read_line_counter() < 5:
                self.cros_line_state()    
                lines = lines - 1
        self.cc.brake()




                    
        
        
        




