#!/usr/bin/env python3

import level1
from time import sleep


class CarBehavior:
    def __init__(self, ti):
        self.target_intesity = ti    
        self.factor = 0.4
        self.cc = level1.CarControl()
        
         

    def lineFollow(self, speed):
         #Scaling down the intensity, expected range: 4 - 46 - 76   
        intensity = self.cc.read_line_sensor()
        if intensity > self.target_intesity:
            speed_correction = round((intensity - self.target_intesity)*self.factor * 1.25)
            self.cc.drive(speed, speed - speed_correction)
        else:                                                                   #0.715 to get range from 42 to 30 on black
            speed_correction = round(((self.target_intesity - intensity))*self.factor * 1.3)
            self.cc.drive(speed - speed_correction, speed)

    
    def cros_line_state(self, next_instruction):
        white = False
        white_counter = 0
        while white == False:
            self.cc.drive(90, 90)
            if next_instruction == "R":
                if self.cc.read_line_counter() > 30:
                    white_counter += 1
                if white_counter > 8:
                    white = True
            elif next_instruction == "L" or next_instruction == "S":
                if self.cc.read_line_counter() > 30:
                    white_counter += 1
                if white_counter > 10:
                    white = True
            



    #Kan være der skal tilføjes så vi kigger på eksempelvis de sidste 5-10 værdier fra line counter sensor
    #før vi registrerer det som en linje (Hvis værdien nu ved en fejl jumper ned til sort)
    def straigt(self, lines, next_instruction):
        while lines > 0:
            print("LINES: ", end = '')
            print(lines)
            self.lineFollow(70)
            print("LINE COUNTER: ", end = '')
            print(self.cc.read_line_counter())
            if self.cc.read_line_counter() < 20:
                self.cros_line_state(next_instruction)                
                lines = lines - 1
        self.cc.brake()