# coding utf-8
"""
A device uses a Stirling cycle on 359 moles of a monatomic
ideal gas between two reservoirs with temperatures of 379 K
and 653 K as a refrigerator or a heat pump.

The volume of the system shifts between 0.67 m^3 and 2.17 m^3.

Part A: ---------------------------------------------------------
How much energy does this device remove from the cold reservoir?

    Assuming that the beginning temperature is one or the other
    variable, we begin to formulate the 2 step process
    for finding the movement of final energy away from the system.

    Changes temperature from 653K to 379K, so we can use the equation:

    heatEnergy
    = specificHeatConstantVolume * number of moles * (Temperature Change)

    Afterwards we have to add the next step's work using constant
    pressure principle in order to obtain the total energy traveled:

    work
    = number of moles * constant R * final temperature *
      math.log(volumeFinal / volumeInitial)

    Add both heatEnergy & work together in order to get the total energy

    = 2556102.59709 J

Part B: -----------------------------------------------------------
How much energy does this device transfer into the hot reservoir?

    Similar to Part A, we do the same procedure in order to solve
    the energy transfer for the hot reservoir.

    Change in Temperature is 379K to 635K, so we can use:

    heatEnergy
    = specificHeatConstantVolume * number of moles * (Temperature Change)

    Afterwards we have to add the next step's work using constant
    pressure principle in order to obtain the total energy traveled:

    work
    = number of moles * constant R * final temperature *
      math.log(volumeFinal / volumeInitial)

    Then add both heatEnergy and work to get total energy
    = 3517255.97472 J


Part C: -----------------------------------------------------------
How much work is done by the device on the gas?

Like all Stirling Cycles, the difference between the added heat and
exited heat is equal to the total work done by gas.

WorkByGas
= HeatIn - HeatOut
= 961153.37763 J

Part D: -----------------------------------------------------------
What is the coefficient of performance of this engine if we use
it to cool a refrigerator?

Using Part A and Part B into the equation to solve the Coefficient...

Coefficient of Realistic Performance for a Refrigerator (heat flows out)
= heat of cold reservoir / work on engine
=

Part E: -----------------------------------------------------------
What is the coefficient of performance of this engine if we use
it as a heat pump?

Using Part A and Part B into the equation to solve the Coefficient...

Coefficient of Realistic Performance for a Heat Pump (heat flows in)
= heat of hot reservoir / work on engine
=

"""
import math

import Constants

if __name__ == '__main__':
    n_moles = 359.0
    lowReservoir = 379.0
    highReservoir = 653.0
    volumeInitial = 0.67
    volumeFinal = 2.17

    firstEnergyToColdReservoir = (
        Constants.SPECIFIC_HEAT_OF_CONSTANT_VOLUME *
        n_moles * (highReservoir - lowReservoir)
    )

    secondEnergyToColdReservoir = (
        n_moles * Constants.R * lowReservoir *
        math.log(volumeFinal / volumeInitial)
    )

    totalEnergyToColdReservoir = (
        firstEnergyToColdReservoir + secondEnergyToColdReservoir
    )

    print totalEnergyToColdReservoir

    thirdEnergyToColdReservoir = (
        Constants.SPECIFIC_HEAT_OF_CONSTANT_VOLUME *
        n_moles * (highReservoir - lowReservoir)
    )

    fourthEnergyToColdReservoir = (
        n_moles * Constants.R * highReservoir *
        math.log(volumeFinal / volumeInitial)
    )

    totalEnergyToHotReservoir = (
        thirdEnergyToColdReservoir + fourthEnergyToColdReservoir
    )

    print totalEnergyToHotReservoir

    gasWork = totalEnergyToHotReservoir - totalEnergyToColdReservoir

    print gasWork

    refrigeratorCoefficient = totalEnergyToColdReservoir / gasWork

    print refrigeratorCoefficient

    heatPumpCoefficient = totalEnergyToHotReservoir / gasWork

    print heatPumpCoefficient
