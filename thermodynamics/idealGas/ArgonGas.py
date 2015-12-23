# coding=utf-8
"""

A tank holds 133 moles of argon gas (atomic mass = 6.633521 × 10-26 kg)
at a pressure of 101300 Pa and a temperature of 302 K. Recall that the
number of gas molecules is equal to Avagadros number (6.022 × 1023)
times the number of moles of the gas

PART A:
What is the volume of the tank?

We can use the equation:

pressure * volume = temperature * number of moles * R constant

And solve specifically for the volume

volume = temperature * number of moles * R Constant / pressure

Plugging in our values and we get:

volume
= 3.29672932569 meters cubed

PART B:
How much kinetic energy is contained in this gas?

In order to solve for the Kinetic Energy we can use the kinetic
energy equation for monatomic moles of:

KE = (3/2) * R * T * per mole

so..
KE
= 3/2 * R * T * number of moles
= 500938.021038 J

PART C:
What is the average speed of one of the argon atoms?

Finding the average speed of one of the argon atoms is
simple using the average molecular speed equation:

average velocity = sqrt (3 * R * T / M)

where M is the molar mass, defined by the mass of Argon times Avogadro's number

plugging in our values and...

averageVelocity
= sqrt( 3 * R * T / M)
= 434.248918461 m/s

PART D:
The escape speed of Earth is 11200 m/s. What temperature would the
argon gas need to have so that the average speed of the gas atoms
was equal to this escape speed?

Again, in this equation we have to work backwards with the given value
and solve for the temperature given the velocity required.

average velocity = sqrt (3 * R * T / M)

solving for T

T = (M * averageVelocity^2)/ (3 * R)
= 200893.320605 K


"""
import Constant
import math

if __name__ == '__main__':
    numberOfMoles = 133
    atomicMassOfArgon = 6.633521 * 10 ** -26
    initPressure = 101300
    initTemp = 302

    molarMass = Constant.AVOGADRO_NUMBER * atomicMassOfArgon

    volume = initTemp * numberOfMoles * Constant.R / initPressure
    print "The volume of the tank is:", volume

    kineticEnergyOfMolecule = 1.5 * initTemp * Constant.R * numberOfMoles

    print "The amount of kinetic energy present in this molecule is:", kineticEnergyOfMolecule

    averageVelocity = math.sqrt(3 * Constant.R * initTemp / (molarMass))

    print "The average velocity of the given molecules is", averageVelocity

    velocityRequiredToEscapeEarth = 11200

    temperatureNeeded = (molarMass * (velocityRequiredToEscapeEarth ** 2)) / (3 * Constant.R)

    print "The temperature needed to escape Earth is:", temperatureNeeded
