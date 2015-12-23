# coding=utf-8
"""
A cylinder with a movable piston contains
13.5 moles of a monatomic ideal gas at a
pressure of 2.06 × 10^5 Pa. The gas is initially
at a temperature of 300 K. An electric heater adds
50600 J of energy into the gas while the piston moves
in such a way that the pressure remains constant.

PART A:
What is the temperature of the gas after the energy is added?

Similar to the last problem, we use the specific heat equation
and solve for the final temperature

Q
= number of moles * specific heat at constant pressure * (tempFin - tempInit)

tempFinal
= (Q / (number of moles * spec heat at constant pressure)) + tempInit
=

PART B:
What is the change in volume of the gas?

Similar to the last problem we can use the Laws of Gases:

initial volume / initial temperature = final volume / final temperature

final volume = initial volume * final temperature / initial temperature

first we must find the initial pressure of the system

initialPressure * initialVolume = temperature * number of moles * R constant

initialVolume = temperature * number of moles * R constant / initialPressure

plugging that value back into the final volume we can
get both values, and then we find the difference of the two to get:

changeInVolume
= finalVolume - initialVolume
= 0.0982342559203 meters cubed

PART C:
How much work is done by the gas during this process?

We can use the equation:

work done by the gas
= change in volume * (-final pressure)
= 20236.2567196 J


"""
import Constant

if __name__ == '__main__':
    tempInitial = 300
    energyGiven = 50600
    n_moles = 13.5
    presInitial = 2.06 * 10 ** 5

    tempFinal = (energyGiven / (n_moles * Constant.SPECIFIC_HEAT_OF_CONSTANT_PRESSURE)) + tempInitial

    print "The final temperature is:", tempFinal

    volInitial = tempInitial * n_moles * Constant.R / presInitial

    volFinal = volInitial * tempFinal / tempInitial

    differenceBetweenVolumes = volFinal - volInitial

    print "The difference of volume is:", differenceBetweenVolumes

    workDoneByGas = presInitial * differenceBetweenVolumes

    print "The work done by the gas is:", workDoneByGas
