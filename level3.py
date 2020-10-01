#!/usr/bin/env python3

###############################################################################
#                       INSTRUCTIONS FROM THE SOLVER                          #                                                                                              
#                                                                             #  
#                                                                             #  
# S = Go straight for 1 line                                                  #
# L = Turn left and go straight for 1 line                                    #           
# R = Turn right and go stright for 1 line                                    #       
# B = Go reverse, make 180 turn and go straight for 1 line                    #
###############################################################################

import level2



class CarIntructions:
    def __init__(self):
        self.cb = level2.CarBehavior(18)
        self.solver_file = open("solver_res.txt")
        self.instruction = self.solver_file.read()


    def preform_instructions(self):
        for i in range(len(self.instruction)):
            if test.instruction[i] == "S":
                s_counter = 1
                while instruction[i + s_counter] == "S"
                    s_counter += 1
                self.cb.straigt(s_counter)
                i += s_counter
            if test.instruction[i] == "L":
                self.cb.cc.turn_left()
                self.cb.straigt(1)
            if test.instruction[i] == "R":
                self.cb.cc.turn_right()
                self.cb.straigt(1)
            if test.instruction[i] == "B": 
                self.cb.cc.turn_arround()
                self.cb.straigt(1)



test.preform_instructions()


print("SLUT")