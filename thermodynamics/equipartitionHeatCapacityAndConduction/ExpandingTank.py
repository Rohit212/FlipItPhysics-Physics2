# coding= utf-8
"""
A 27-m3 tank is filled with 2590 moles of an ideal gas.
The temperature of the gas is initially 300 K, but it is raised to 735 K.

PART A:
What is the change in the pressure of the gas inside the tank?

We can use the ideal gas law equations in order to solve for
the final pressure and then use the standard specific
heat law in order to solve for the Q in the equation

volume initial * pressure initial = temperatureInitial * number of moles * R constant

pressure initial = temperatureInitial * number of moles * R Constant / volume initial

pressureFinal / temperatureFinal = pressureInitial / temperatureInitial

pressureFinal = temperatureFinal * pressureInitial / temperatureInitial

changeInPressure
= pressureFinal - pressureInitial
= 346944.022678 Pa

PART B:
Let's assume that the tank is made out of a material which
has a coefficient of linear expansion of 6.5 × 10-5 K-1, and
that the temperature of the tank is always the same as the
temperature of the gas. Remember that the space inside the
tank will expand as if it were made of the material surrounding
it. What is the change in the volume of the tank due to the
increase in temperature from 300 K to 735 K?

We can use the coefficient of linear expansion for volume:

(finalVolume - initialVolume)/ initialVolume
= 3 * linearCoefficient * (tempFinal - tempInit)

We can plugin to the system and solve for the change in volume of the system:

changeInVolume
= 3 * linearCoefficient * initialVolume * (tempFinal - tempInit)
= 2.290275 meters cubed

PART C:
Given that the tank expands a bit, what is the actual change
in the gas pressure due to the increase in temperature?

We know that the volume changed 2.290275 meters from
initial volume, so we can obtain our final pressure:

pressureFinal = number of moles * R constant * tempFinal / volumeFinal

changeInPressure
= pressureFinal - pressureInitial
= 301106.443298 Pa


"""
import Constant

if __name__ == '__main__':
    volInit = 27.0
    numberOfMoles = 2590.0
    tempInit = 300.0
    tempFinal = 735.0

    presInit = (numberOfMoles * Constant.R * tempInit) / volInit

    presFinal = tempFinal * presInit / tempInit

    changeInPressure = presFinal - presInit

    print "The change in pressure in the system is:", changeInPressure

    coefficientOfExpansion = 6.5 * (10 ** -5)

    changeInVolume = (
        3 * coefficientOfExpansion * volInit * (tempFinal - tempInit)
    )

    print "The change in volume of the system is:", changeInVolume

    volumeFinal = volInit + changeInVolume

    presFinal = numberOfMoles * Constant.R * tempFinal / volumeFinal

    changeInPressure = presFinal - presInit

    print "The actual change in pressure is:", changeInPressure
