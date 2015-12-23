# coding=utf-8
"""

A beam used in construction is made of steel, which
has a coefficient of linear expansion of 1.3 × 10-5 K-1.
The beam is 29 m long at a temperature of 1634 K when it
is made. As it cools, the temperature of the beam
decreases to 299 K.

PART A:
What is the change in the length of the beam due to cooling?

We can use the linear expansion formula and plugin
in order to solve for the total change in the length:

change in length
= coefficient of linear expansion * (tempFinal - tempInitial) * LengthInitial
= -0.503295


PART B:
If the mass of the steel beam is 377 kg and the specific heat
capacity of steel is 490 J/kg-K, how much energy did the steel
beam lose due to cooling? (Use a positive value for the amount
of energy.)

Using the specific heat equation we can solve to be:

Q
= specific heat of steel * (tempFinal - tempInit) * mass of steel beam
= 246614550
"""
if __name__ == '__main__':
    coefficientOfLinearExpansion = 1.3 * 10 ** -5
    initialLength = 29
    initialTemp = 1634
    finalTemp = 299

    changeInLength = (
        coefficientOfLinearExpansion * (finalTemp - initialTemp) * initialLength
    )

    print "The total change in length is:", changeInLength

    specificHeatOfSteel = 490
    massOfSteel = 377

    energyChange = specificHeatOfSteel * massOfSteel * (finalTemp - initialTemp)

    print "The total amount of change in energy is:", -1 * energyChange

