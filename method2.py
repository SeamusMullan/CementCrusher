## Imports
import matplotlib.pyplot as plt
import numpy
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


import random

line = [i for i in range(0,100)]


data = []

for i in range(0,1000):
    data.append(i + random.randint(0, 99))

data = numpy.array(data)
data = numpy.convolve(data, line, mode='same')

print(data)

def method2():
    """
    Assume that the strength changes with the amount of water to a certain point, and then drops off
    Also assume that the mix is useless below a certain threshold (eg: >20% water)

    Use stress-strain curve to find the yield point of the mix at the points and return the strongest mix
    Graph the results and highlight the strongest mix
    """

    # Find the yield point for the mix at the points
    yield_points = []
    temp1 = 0
    threshold = 20

    for i in data:
        ## find the yield point where the stress strain curve jumps rapidly
        if temp1 - i > threshold:
            yield_points.append(i)
        temp1 = i


    top = 0
    # Find the mix with the highest yield point
    for i in yield_points:
        if i > top:
            top = i
    maxPoint = top

    # Plot the stress strain graph and highlight the highest and lowest yield points
    plt.plot(data)
    plt.axhline(y=maxPoint, color='r', linestyle='dotted') # Strongest mix
    plt.show()




method2()