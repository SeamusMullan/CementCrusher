## Imports
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy
import random
from scipy.stats import linregress
import pprint

figure(figsize=(10, 6))
# from pytest import yield_fixture

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



"""
Assume that the strength changes with the amount of water to a certain point, and then drops off
Also assume that the mix is useless below a certain threshold (eg: >20% water)

Use stress-strain curve to find the yield point of the mix at the points and return the strongest mix
Graph the results and highlight the strongest mix
"""




## GRAPH PLOTTING

def plotgraph(waterPercent, x):
    prediction_line = [i*(waterPercent/100) for i in range(0,100)]    

    data = []
    for i in range(0, 1000):
        data.append(i + random.randint(0,100))
    data = numpy.array(data)
    data = numpy.convolve(data, prediction_line, mode='same')

    data = [i for i in data * (waterPercent/100)]
    ## AFFECT BASED ON WATER %

    # print(data)

    slope, intercept, r, p, se = linregress(prediction_line[0:50], data[0:50])
    print(slope*1e-2)

    ## YIELD POINTS

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
    plt.plot(data, label=f'{waterPercent}% Water - {round(slope*1e-2, 2)} GPa')
    # plt.axhline(y=maxPoint, color='b', linestyle='dotted') # Strongest mix
    leg = plt.legend(loc='best')
    plt.title("Stress / Strain (Compressive Strength)")

    plt.savefig(f'figs/graph{x}.png')





def main():

    ## WATER PERCENTAGE
    waterPercent = [i for i in range(0, 110, 10)]

    ## STRESS-STRAIN GRAPH
    for i in waterPercent:
        plotgraph(i, i)


if __name__ == '__main__':
    main()