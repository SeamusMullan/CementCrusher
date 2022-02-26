## Imports
#import scipy
#import numpy as np
import matplotlib.pyplot as plt
import math

## Properties of normal Portland Cement Concrete (Sources at botttom)
"""
Density = 2300 
Compressive_strength = 30
Flexural_strength = 4
Tensile_strength = 3.5
Modulus_of_elasticity = 27
Permeability = 1 x 10^-10
# Coefficient of thermal expansion = 10-5 oC-1 (5.5 x 10-6 oF-1)
Drying_shrinkage = 6 x 10^-4
Drying_shrinkage_reinforced_concrete= 2.5 x 10-4
Poissons_ratio = 0.20
Shear_strength = 11.5
# Specific heat - c =  0.75 kJ/kg K (0.18 Btu/lbm oF (kcal/kg oC))

"""
## Da code


def waterAmtForWeight(cementWeight, ratio): # ration between 0.1 and 1.0
    return (cementWeight*ratio)

points = []

for i in range(1,100):
    concreteAmount = 100
    x = i/1
    y = waterAmtForWeight(concreteAmount, x)
    points.append(y)


plt.plot(points)
plt.ylabel("da points")
plt.show()











## Sources=
# https=//www.engineeringtoolbox.com/concrete-properties-d_1223.html
# https=//civilengineeringbible.com/article.php?i=14
