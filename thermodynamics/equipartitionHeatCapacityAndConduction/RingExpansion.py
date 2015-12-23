# coding= utf-8
"""
An aluminum washer has an outer radius
ro = 1.35 cm and an inner radius of ri = 0.43 cm.
The temperature of the washer is raised from 284 K to 635 K.

PART A:
If the mass of the washer is 0.033 g,
the molar mass of aluminum is 26.98 g/mol,
and the molar specific heat of aluminum is 24.3 J/mol-K,
what is the change in the internal energy of the washer?

Internal Energy is given the specific heat equation:

Internal Energy
= number of moles * specificHeatOfAl * change in temperature

In order to find the number of moles we divide mass of given over molar mass

numberOfMoles = massOfGivenAl / molarMassOfAl

Now we can easily solve for Q:
= 10.4324277242 J

PART B:
If the coefficient of linear expansion of aluminum is
2.22 × 10-5 K-1, what is the change in the outer
radius of the aluminum washer?

Length of Expansion for Radius:
Length of Expansion = Length of outer radius * coefficient of linear expansion * (tempFinal - tempInitial)

OuterRadiusChange
= 0.01051947


PART C:
What is the change in the inner radius of the aluminum washer?

Length of Expansion for Radius:
Length of Expansion = Length of inner radius * coefficient of linear expansion * (tempFinal - tempInitial)

InnerRadiusChange
= 0.003350646


PART D:
What is the change in area of the washer?

Formula for area of a circle
= 0.5 * 3.14159 * (change in inner radius - change in outer radius)^2 * 1000 to convert units


We can find the the area of expansion by finding both of the radius'
expansions and then find the difference between both of the values

So first we must solve the change of the inner radius
then solve for the change in outer radius

And then plugin those values into the formula of a circle
Circle
= changeInArea = 0.5 * pi * (changeInOuterRadius - changeInInnerRadius)^2 * 1000
= 0.080726423799


"""
import math

if __name__ == '__main__':
    initialMassOfWasher = 0.033
    molarMassOfAl = 26.98
    molarSpecificHeatOfAl = 24.3
    radiusInner = 0.43
    radiusOuter = 1.35
    tempInitial = 635
    tempFinal = 284
    coefficientOfLinearExpansion = 2.22 * 10 ** -5

    numberOfMoles = initialMassOfWasher / molarMassOfAl

    internalEnergy = numberOfMoles * molarSpecificHeatOfAl * (tempFinal - tempInitial)

    print "The amount of internal energy transfered is:", -1 * internalEnergy

    outerRadiusChange = radiusOuter * coefficientOfLinearExpansion * (tempFinal - tempInitial)

    print "The outer change in radius is:", -1 * outerRadiusChange

    innerRadiusChange = radiusInner * coefficientOfLinearExpansion * (tempFinal - tempInitial)

    print "The inner change in radius is:", -1 * innerRadiusChange

    changeInArea = 0.5 * math.pi * ((outerRadiusChange - innerRadiusChange) ** 2) * 1000
    print "The total change in area is:", changeInArea
