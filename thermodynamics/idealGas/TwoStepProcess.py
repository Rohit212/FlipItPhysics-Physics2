# coding=utf-8
"""
Suppose that 4.7 moles of a monatomic ideal gas
(atomic mass = 8.4 × 10 ^ -27 kg)  are heated
from 300 K to 500 K at a constant volume of 0.47 m^3.

PART A:
How much energy is transferred by heating during this process?

Since the following question shows that their is a constant
volume we can use the specific heat of constant volume
to quickly solve the problem:

Q
= specificHeatConstantOfVolume * number of moles * temperature
=


PART B:
How much work is done by the gas during this process?

Since the volume stays constant, there is 0 work done by
the gas.

ZERO

PART C:
What is the pressure of the gas once the final temperature has been reached?

In order to find final pressure we can use the Gas Laws

pressure final / temp final = pressure initial / temp initial

pressure final = temp final * pressure initial / temp initial

Now we need to find out the initial pressure by using the ideal gas law:

pressure * volume = number of moles * R constant * temperature

pressure
= number of moles * R constant * temperature / volume

Now that we have our own initial pressure, we can plug it
back into the system and solve for the final pressure of the
system

pressure final
= tempFinal * pressure initial / temp initial
=

PART D:
What is the average speed of a gas molecule after the final
temperature has been reached?

In order to find the average speed of the molecule we
can use the average speed formula:

v(avs) = sqrt(3 * R * temperature final / molarMass)

molarMass
= atomicMassOfAmu * numberOfMolars

and then solve the equation with our given values

v(avs)
=


PART E:
The same gas is now returned to its original temperature using a process
that maintains a constant pressure. How much energy is transferred by
heating during the constant-pressure process?

We can simple use the specific heat of constant pressure and use the
specific heat equation:

Q
= specificHeatOfConstantPressure * (tempFinal - tempInit) * numberOfMoles
=


PART F:
How much work was done on or by the gas during the constant-pressure process?

We can do this by using the work equation:

netWorkEquation = finalPressure * change in volume

the only requiremenet we now need to have is the final volume
after the constant pressure process

our inintial volume is now defined as:

0.47 meters cubed

pressure * volume = n * R * T
volumeFinal
= number of moles * R Constant * temperature final / pressureFinal
=

Then we can find the change in volume times the final pressure to obtain the work:

netWorkEquation
= finalPressure * change in volume
=


"""
import Constant
import math

if __name__ == '__main__':
    numberOfMoles = 4.7
    atomicMass = 8.4 * (10 ** -27)
    initialVolume = 0.47
    initialTemperature = 300.0
    finalTemperature = 500.0

    energyTransferredIntoSystem = (

        Constant.SPECIFIC_HEAT_OF_CONSTANT_VOLUME * numberOfMoles *
        (finalTemperature - initialTemperature)
    )

    print "The amount of energy transferred into the system:", energyTransferredIntoSystem

    print "The amount of work done by the gas in the first process is zero because of no change in volume."

    initialPressure = numberOfMoles * Constant.R * initialTemperature / initialVolume

    finalPressure = finalTemperature * initialPressure / initialTemperature

    print "The final pressure of the system after the first process is:", finalPressure

    averageSpeed = math.sqrt(

        (3 * Constant.R * finalTemperature) /
        (atomicMass * Constant.AVOGADRO_NUMBER)
    )

    print "The average speed of the molecule is:", averageSpeed

    energyTransferred = (
        Constant.SPECIFIC_HEAT_OF_CONSTANT_PRESSURE *
        (initialTemperature - finalTemperature) *
        numberOfMoles
    )

    print "The amount of energy transferred during constant pressure is:", energyTransferred

    volumeFinal = numberOfMoles * Constant.R * initialTemperature / finalPressure

    netWork = (initialVolume - volumeFinal) * finalPressure

    print "The amount of work done by the gas during the 2nd part is:", netWork

    print "The graph defined by a lines connecting perpendicularly, moving from cold to high to cold temperature."
