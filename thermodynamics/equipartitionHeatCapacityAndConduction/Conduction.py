# coding= utf-8
"""
A hot reservoir with a temperature of 706 K is 0.43 m away
from a cold reservoir with a temperature of 362 K. The two
reservoirs are insulated from each other except for a rod
of brass (k = 109 W/m-K) that has a cross-sectional area
of 0.043 m2. The entire system is allowed to reach a
steady-state condition.

PART A:
How much energy is transferred by heat between the
hot reservoir and the cold reservoir in ten minutes?

We are asked how much energy transfers within the said system in 10mins

We know that in this system, the units of specific heat are Watts
meaning that for 109 (Joules/second)m-K which we must convert:

109 * 60(seconds per min) = 6540 J/m * K

Using the newly found K, we can multiple by the change in temperature

Internal Energy
= K * (finalTemp - initTemp)
=

PART B:
Assume that you need to transfer 4726760 J of energy in
ten minutes between the two reservoirs. To enhance the
rate of energy transfer, a steel rod (k = 43 W/m-K) of
the same length is added between the two reservoirs.
What should the cross-sectional area of the steel rod
be in order to achieve the proper rate of energy transfer?

First we must subtract the amount of heat the is already transferred
through the first set of poles, which was the last value

The area of an object with the latent heat of linearization is:
Q = k * A * (finalTemp - initTemp)/ length

Solve for area...

A = Q * length / (k * (finalTemp - initTemp) * timeNeeded)

With our new value we can begin to solve for the A in our equation

A
= Q * lengthOfROd / (k * (tempFin - tempInit) * time)
=
"""

if __name__ == '__main__':
    hotTemp = 706
    coldTemp = 362
    k = 109
    transformedKToC = k * 60

    internalEnergy = transformedKToC * (hotTemp - coldTemp)

    print "The total amount of energy that has transformed:", internalEnergy

    newK = 43
    desiredQ = 4726760
    time = 60 * 10
    lengthOfRod = 0.43
    actualValue = desiredQ - internalEnergy

    sizeOfArea = actualValue * lengthOfRod / (newK * (hotTemp - coldTemp) * time)

    print "The required size of the area in order to obtain the desired energy transfer is:", sizeOfArea
