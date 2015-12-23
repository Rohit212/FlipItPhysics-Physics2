# coding= utf-8
"""
A historian claims that a cannonball fired at a castle wall would
melt on impact with the wall. Let's examine this claim. Assume
that the kinetic energy of the cannonball is completely transformed
into the internal energy of the cannonball on impact with no energy
transferred to the wall. The cannonball is made of iron, which has a
 specific heat capacity of 450 J/kg-K and a melting point of 1811 K.


PART A:
If the cannonball has an initial temperature of 305 K,
how fast would the cannonball need to travel in order
to reach its melting point on impact?

Heat energy directly links to the amount of kinetic energy
an object has. This cannonball would need a specific amount
of energy which we can solve via the ideal gas law.

Q = specific heat * temperature difference * massOfCannonBall

We can compare it's required speed using the Kinetic Energy formula
since all of the energy will transform into internal energy

1/2 * mass of cannonball * velocity^2

Our goal is to solve for the velocity, so we can set both equations
equal to one another and solve for velocity, lets do this now:

1/2 * mass of ball * velocity squared
= specificHeat * temperature difference * mass of cannonball [cancel out cannonball mass]

velocity ^ 2 = 2 * specificHeat of CB * tempDifference

velocity = sqrt (specifcHeat of CB * 2 * tempDifference)

Now we plug in our given values to get:

velocity
= 1164.21647472 m/s

PART B:
If the latent heat of fusion of iron is 2.72 × 10 ^ 5 J/kg,
how fast would the cannonball need to travel in order to
reach its melting point AND completely transform into
liquid iron on impact?

So this is similar to the last problem, the only difference is that
in the equation for heat energy we must add the heat of fusion * mass of
the cannon ball


Q = specific heat * temperature difference * massOfCannonBall + massOfCannonBall * latentHeatOfFusionForCB
Q = massOfCannonBall(specificHeat * tempDiff + latentHeatOfFusion)

Solve using the same KE formula:

1/2 * massOfCB * velocity ^ 2 = massOfCannonBall(specificHeat * tempDiff + latentHeatOfFusion)

Solve for velocity again to get...

velocity
= sqrt(2(specificHeat * tempDiff + latentHeatOfFusion))
= 1378.18721515 m/s

"""
import math

if __name__ == '__main__':
    initialTemp = 305
    finalTemp = 1811
    specificHeatOfCB = 450

    velocity = math.sqrt(specificHeatOfCB * 2 * (finalTemp - initialTemp))

    print "The velocity required to melt on impact is:", velocity

    latentHeatOfFusion = 2.72 * 10 ** 5

    velocity = math.sqrt(2 * (specificHeatOfCB * (finalTemp - initialTemp) + latentHeatOfFusion))

    print "The velocity required to melt on impact in addition to latent heat is:", velocity
