#!/usr/bin/env python3

#Venstre motor går til OUTPUT_A, højre OUTPUT_B,

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2,INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, LightSensor, GyroSensor
from time import sleep
from ev3dev2.sound import Sound

class CarControl:
    def __init__(self):
        self.tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)
        self.steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B)
        self.line_sensor = ColorSensor(INPUT_2)
        self.line_counter = ColorSensor(INPUT_3)
        self.sound = Sound()
        self.gyro = GyroSensor(INPUT_1)
        self.gyro.reset()
        self.dir_state = "S"


    def drive(self, l_speed, r_speed):
        self.tank_pair.on(left_speed=l_speed, right_speed=r_speed)

    def reverse(self):
        self.tank_pair.on_for_degrees(left_speed = -90, right_speed = -90, degrees = 360, brake = True)

    def brake(self):
        self.tank_pair.off(brake = True)

    def turn_left(self):
        self.steer_pair.on_for_degrees(steering = -100, speed = 90, degrees=180, brake=True)

    def turn_right(self):
        self.steer_pair.on_for_degrees(steering = 100, speed = 90, degrees=170, brake=True)

    def turn_arround(self):
        self.steer_pair.on_for_degrees(steering = -100, speed = 90, degrees = 370, brake = True)

    def read_line_sensor(self):
        return (self.line_sensor.reflected_light_intensity)
    
    def read_line_counter(self):
        return (self.line_counter.reflected_light_intensity)

    def play_sound(self):
        self.sound.beep()

    def read_gyro(self):
        return self.gyro.angle

    def turn_left_new(self):
        self.tank_pair.on(left_speed = -90, right_speed = 90)
        if self.dir_state == "S":
            while True:
                if self.read_gyro() <= -90:             #Ikke sikker på at den altid kan læse ved præcist -90
                    self.tank_pair.off(brake = True)
                    self.dir_state ="L"
                    return 0
        elif self.dir_state == "L":
            while True:
                if self.read_gyro() == 180 or self.read_gyro() == -180:
                    self.steer_pair.stop()
                    self.dir_state = "B"
                    return 0
        elif self.dir_state == "B":
            while True:
                if self.read_gyro() == 90 or self.read_gyro() == -270:
                    self.steer_pair.stop()
                    self.dir_state = "R"
                    return 0
        elif self.dir_state == "R":
            while True:
                if self.read_gyro() == 0 or self.read_gyro == -360 or self.read_gyro == 360:
                    self.gyro.reset()
                    self.steer_pair.stop()
                    self.dir_state = "S"
                    return 0


    def turn_right_new(self):
        self.steer_pair.on(90,90)
        print("JEG ER HER")
        if self.dir_state == "S":
            while True:
                if self.read_gyro == 90:
                    self.steer_pair.stop()
                    self.dir_state = "R"
                    return 0
        elif self.dir_state == "L":
            while True:
                if self.read_gyro() == 360 or self.read_gyro() == 0:
                    self.gyro.reset()
                    self.steer_pair.stop()
                    self.dir_state = "S"
                    return 0
        elif self.dir_state == "B": 
            while True:
                if self.read_gyro() == 270 or self.read_gyro == -90:
                    self.steer_pair.stop()
                    self.dir_state == "R"
                    return 0
        elif self.dir_state == "R":
            while True:
                if self.read_gyro() == 180 or self.read_gyro() == -180:
                    self.steer_pair.stop()
                    self.dir_state == "B"
                    return 0

            


    
