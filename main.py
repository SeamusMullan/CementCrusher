from scipy import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
from math import *

## Summary:
# This is the main file for the simulation.
# It creates a grid of particles representing the structure of cement.
# It then applies a force to the particles to simulate the movement of the cement under compression.
# The particles are then animated to show the movement of the cement.
# The force is applied for a certain amount of time or until a % of the particles have moved a certain distance from their original position.
# This is repeated multiple times with different water levels to simulate the movement of cement under different water levels.
# The results are then plotted to show the movement of the cement under different water levels.
# The best result will be the result in which the least movement occurs.




class Particle:
    def __init__(self, x, y, ax, ay, mass, attraction):
        # Position
        self.x = x
        self.y = y
        # Mass
        self.mass = mass
        # Acceleration
        self.ax = 0
        self.ay = 0
        # Velocity
        self.vx = 0
        self.vy = 0
        # Other Forces
        self.attraction = attraction
        # Original Position
        self.original_x = x
        self.original_y = y

        
    def repel(self, other):
        # Calculate the distance between the two particles
        distance = sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        # If the particles are too close, apply a force to push them apart
        if distance < 0.5:                                                          ### TODO: Change this to a variable
            theta = atan2(other.y - self.y, other.x - self.x)
            force = self.mass * other.mass / distance ** 2
            self.ax += force * cos(theta)
            self.ay += force * sin(theta)

    def attract(self, other):
        # Calculate the distance between the two particles
        distance = sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        # If the particles are too close, apply a force to push them apart
        if distance < 0.5:                                                          ### TODO: Change this to a variable
            theta = atan2(other.y - self.y, other.x - self.x)
            force = self.mass * other.mass / distance ** 2
            self.ax -= force * cos(theta)
            self.ay -= force * sin(theta)

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

    def addForce(self, x, y):
        self.ax += x
        self.ay += y

    def update(self):


    # Gravity Last
    def gravity(self):
        self.ax += 0
        self.ay += -9.81