# coding=utf-8
"""
A 8.5-kg cube of copper (cCu = 386 J/kg-K) has a temperature of 750 K.
It is dropped into a bucket containing 5.1 kg of water
(cWater = 4186 J/kg-K) with an initial temperature of 293 K.

PART A:
What is the final temperature of the water-and-cube system?

Simple set up in the ideal gas equation and using the laws of
thermodynamics to solve for the temperature final of the system

0 = (tf(system)- initialTempOfCu) * massOfCopper * specificHeat Of Copper +
    (tf(system)- initialTempOfWater) * massOfWater * specificHeat Of Water

Solving for tF of system and plugging in:

tfSystem =
  [(mass of Copper * specific Heat Of Copper * ti(Cu)) +
  (mass of Water * specific Heat Of Water * ti(Water))]
  /
  (mass of Copper * specific Heat Of Copper + mass of Water * specific Heat of Water)

= 353.8786582 K

PART B:
If the temperature of the copper was instead 1350 K, it
would cause the water to boil. How much liquid water
(latent heat of vaporization = 2.26 × 106 J/kg) will
be left after the water stops boiling?

With the new initial temperature of water and
the added situation of Latent Heat of Vaporization
for water, we must also plugin the value into our
setup equation and set the final temperature to be
surrounding the value of boiling, 373.15:

Latent Heat Of Vaporization Equation [need to add into equation]:
Heat Energy = mass of property * latentHeatOfVaporization

Finally we solve for the mass of material that was created with these
energies:

0 = (tf(system)- initialTempOfCu) * massOfCopper * specificHeat Of Copper +
    (tf(system)- initialTempOfWater) * massOfWater * specificHeat Of Water +
    massOfMaterial * latentHeatCoeffcient(latentHeatOfVaporization)

mass Of Material vaporized
=
    -[tf(system)- initialTempOfCu) * massOfCopper * specificHeat Of Copper +
     tf(system)- initialTempOfWater) * massOfWater * specificHeat Of Water] /
     latentHeatCoefficient

= 0.661041840708 kg

Which is the amount of water that actually vaporized.
The question asks about the amount of water that was left, not the amount
that as actually vaporized so we subtract from the total amount of water:

amount Of Water Left = initial Mass of Water - mass of Material vaporized
amount Of water Left
= 4.43895815929

PART C:
Let's try this again, but this time add just the minimum
amount of water needed to lower the temperature of the copper
to 373 K. In other words, we start with the cube of copper
at 750 K and we only add enough water at 293 K so that it
completely evaporates by the time the copper reaches 373 K.
Assume the resulting water vapor remaining at 373 K.
How much water do we need ?

So in this question we need to solve for the minimum
amount of water needed to get copper to reduce to about
373K. It is similar to the last problem except that all we
require to solve for is the mass or M in the equation
of latent Heat

Our goal is to solve for the total amount of water needed for reducing
the mass of copper down to the required amount. We can simply just set the
latentHeat, the ideal gas equation for copper and water, then solve for
amount of water required

0 = tf(system)- initialTempOfCu) * massOfCopper * specificHeat Of Copper +
     tf(system)- initialTempOfWater) * massOfWater * specificHeat Of Water +
    massOfWater * latentHeatCoeffcient(latentHeatOfVaporization)

solve for mass of water

0 = massOfWater *
    [ (tf(system) - initialTempOfWater) * specificHeat of Water + latentHeatOfCoefficient ]
    + (tf(system)- initialTempOfCu) * massOfCopper * specificHeat Of Copper)

massOfWater = -1 * (tf(system)- initialTempOfCu) * massOfCopper * specificHeat Of Copper) /
            [ (tf(system) - initialTempOfWater) * specificHeat of Water + latentHeatOfCoefficient ]

massOfWater = 0.47637876579

"""

if __name__ == '__main__':
    massOfCu = 8.5
    specificHeatOfCu = 386
    initialTempOfCu = 750

    massOfWater = 5.1
    specificHeatOfWater = 4186
    initialTempOfWater = 293

    finalTempOfCopperAndWater = (

        ((massOfCu * specificHeatOfCu * initialTempOfCu) + (massOfWater * specificHeatOfWater * initialTempOfWater)) /
        (massOfCu * specificHeatOfCu + massOfWater * specificHeatOfWater)

    )

    print "The final temperature of the Water and Copper is:", finalTempOfCopperAndWater

    initialTempOfCu = 1350
    finalTemperatureOfSystem = 373.15
    latentHeatCoefficientOfWater = 2.26 * 10 ** 6

    massOfMaterial = (
        -1 * (
            (finalTemperatureOfSystem - initialTempOfCu) * massOfCu * specificHeatOfCu +
            (finalTemperatureOfSystem - initialTempOfWater) * massOfWater * specificHeatOfWater
        ) /
        latentHeatCoefficientOfWater
    )

    amountOfWaterLeft = massOfWater - massOfMaterial
    print "The total amount of water left after vaporizaton is:", amountOfWaterLeft

    initialTempOfCu = 750

    massOfWater = -1 * (

        (finalTemperatureOfSystem - initialTempOfCu) * massOfCu * specificHeatOfCu /
        ((finalTemperatureOfSystem - initialTempOfWater) * specificHeatOfWater + latentHeatCoefficientOfWater)

    )

    print "The total amount of water required is:", massOfWater
