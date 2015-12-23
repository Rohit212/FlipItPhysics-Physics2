"""
A 4.1-kg block of ice originally at 263 K is placed in thermal
contact with a 13-kg block of silver  (cAg = 233 J/kg-K) which
is initially at 1062 K. The H2O - silver system is insulated
so no heat flows into or out of it.

At what temperature will the system achieve equilibrium?


How much of the mass will actually be converted into vaporization energy
and how much ice will be left?

from last question we can obtain the amount of energy that will
be transformed into mass:

Similar to the last question, we must use the ideal gas
law and latent heat of vaporization in one equation
and solve for the final temperature of the system.

But first we must find out the final temperature of our Silver.

Solving for temperature of Silver:

newTempOfSilver = originalTempOfSilver - [
    ((tempOfWater - tempOfIce) * specificHeatOfIce * massOfIce) /
    (specificHeatOfSilver * massOfSilver)
                                        ]
And our new temp of ice is:
tempOfWater 273.15
since all of our ice completely melted into water
both masses are equal to each other
water mass = ice mass

Now we solve for temp final of both materials in order to get answer:

0 = (tfOfSystem - tempOfWater) * mass Of Water * specificHeatOfWater +
    (tfOfSystem - newTempOfSilver) * mass Of Silver * specificHeatOfSilver) +
    latentHeatOfIce * massOfIceMelted


-(latentHeatOfIce * massOfIce) + (tempOfWater * massOfWater * specificHeatOfWater)
+ (tempOfSilver * massOfSilver * specificHeatOfSilver)
= tempOfSystem( massOfIce * specificHeatOfIce + massOfSilver * specificHeatOfSilver )

tempOfSystem
= [ -(latentHeatOfIce * massOfIce) + (tempOfWater * massOfWater * specificHeatOfIce)
    + (newTempOfSilver * massOfSilver * specificHeatOfSilver) ]
  /
  ( massOfWater * specificHeatOfWater + massOfSilver * specificHeatOfSilver )
= 319.196527021 K


PART B:
What will be the phase of the H2O at equilibrium?

The obvious answer is liquid since the final temperatures
ended up being in the liquid zone for degrees kelvin.

"""

if __name__ == '__main__':
    massOfIce = 4.1
    tempOfIce = 263.0
    specificHeatOfIce = 2093
    latentHeatOfIce = 3.34774 * (10 ** 5)

    massOfSilver = 13.0
    tempOfSilver = 1062.0
    specificHeatOfSilver = 233.0

    tempOfWater = 273.15

    tempOfSilver -= (tempOfWater - tempOfIce) * specificHeatOfIce * massOfIce / (specificHeatOfSilver * massOfSilver)

    specificHeatOfWater = 4186

    finalTempOfSystem = (
        (
            (-1 * latentHeatOfIce * massOfIce) + (tempOfWater * massOfIce * specificHeatOfWater) +
            (tempOfSilver * massOfSilver * specificHeatOfSilver)
        ) /

        ((massOfIce * specificHeatOfWater) + (massOfSilver * specificHeatOfSilver))
    )
    print finalTempOfSystem

