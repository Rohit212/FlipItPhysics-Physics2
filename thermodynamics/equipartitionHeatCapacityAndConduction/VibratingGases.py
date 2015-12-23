# coding= utf-8
"""
Suppose that 1.7 moles of an ideal diatomic gas
has a temperature of 1119 K, and that each molecule
has a mass 2.32 × 10-26 kg and can move in three
dimensions, rotate in two dimensions, and vibrate
in one dimension as the bond between the atoms
the number of gas molecules is equal to Avagadros
number (6.022 × 1023) times the number of moles of the gas.


PART A:
How many degrees of freedom does each molecule of the gas have?

Each molecule normally has 3 degrees of freedom, plus two degrees of
rotation and an additional degree of vibration to total a
degree of freedom 6.


PART B:
What is the internal energy of the gas?

Internal Energy is simply requiring the internal energy
equation using the Freedom Of Degrees equation and plugin:

Internal Energy
= (F / 2) * number of moles * R constant * temperature initial
= 6/2 * numberOfMoles * R constant * temperature initial
=  47449.8031878 J

PART C:
What is the average translational speed of the gas molecules?

The average translational speed equation isdefined as:

average translational speed = sqrt(3 * R constant * temperature / molar mass)

Now we plug in our values and solve for value:

=  1413.44325912 m/s

PART D:
The gas cools to a temperature 547K, which causes the
gas atoms to stop vibrating, but maintain their
translational and rotational modes of motion.

What is the change in the internal energy of the gas?

First we must find our new internal energy with 1 degree of freedom less
and  lower temperature

newInternalEnergy
= (F / 2) * number of moles * R constant * temperature initial
= (5 / 2) * number of moles * R constant * new temperature


Using our previous internal energy value, we can find the
difference between the new and old internal energy values
in order to solve for the change to get:

= -28120.7576533 J

"""
import Constant
import math

if __name__ == '__main__':
    print "The number of degrees of freedom for the molecule are: 6"

    numberOfMOles = 1.7
    initTemp = 1119
    molarMass = 2.32 * 10 ** -26
    internalEnergy = (3 * numberOfMOles * Constant.R * initTemp)

    print "The total internal energy of the system initially is:", internalEnergy

    vRMS = math.sqrt(3 * Constant.R * initTemp / (molarMass * Constant.AVOGADRO_NUMBER))

    print "The translation speed of the atom is:", vRMS

    newTempOfGas = 547
    newInternalEnergy = (2.5 * numberOfMOles * Constant.R * newTempOfGas)

    internalEnergyChange = newInternalEnergy - internalEnergy

    print "The change in internal energy is:", internalEnergyChange
