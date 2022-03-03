## Imports
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy

## Properties of normal Portland Cement Concrete

# Density = 2300 
# Compressive_strength = 30
# Flexural_strength = 4
# Tensile_strength = 3.5
# Shear_strength = 11.5

## Sources with units
# https://www.engineeringtoolbox.com/concrete-properties-d_1223.html
# https://civilengineeringbible.com/article.php?i=14



## Predictions

# Control Data for 100kg cube of Portland cement concrete
Final_weight = 100

Density = 2300
Compressive_strength = 30
Flexural_strength = 4
Tensile_strength = 3.5
Shear_strength = 11.5




def method1():
    """
    Assume that amount of water is directly proportional to compressive strength
    eg: when there is 50% less water, strength decreases by 50%

    Don't bother with stress-strain curve, just assume that the strength is directly proportional to the amount of water
    """
    


    # Calculations
    for i in range(0, 100):
        water_percent = i
        water_weight = water_percent * Final_weight / 100
        cement_weight = Final_weight - water_weight
        
        # Compressive Strength
        compressive_strength = cement_weight * Density * Compressive_strength / Final_weight

    