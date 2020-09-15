#!/usr/bin/env python3
import random
import copy
class Hat:

    def __init__(self,**kwargs):
        self.contents = []

        for key,value in kwargs.items():
            for i in range (value):
                self.contents.append(key)

    def draw (self,number):
        ball_drawn = []

        if number >= len(self.contents):
            return self.contents
        else:
            for i in range (number):
                ball_picked = random.choice(self.contents)
                ball_drawn.append(ball_picked)

                self.contents.pop (self.contents.index(ball_picked))

        return ball_drawn

#-------------------------------------------------------------------------------------

def experiment(hat, balls_to_draw, num_balls_drawn, num_experiments):
    successes = 0
    for _  in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        
        num_of_correct_colors = 0
        for color in balls_to_draw.keys():
            if balls.count(color) >= balls_to_draw[color]:
                num_of_correct_colors += 1
        if num_of_correct_colors == len(balls_to_draw):
            successes += 1
    probability = float(successes)/num_experiments
    return(probability)
