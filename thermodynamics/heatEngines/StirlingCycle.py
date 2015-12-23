# coding=utf-8
"""
Stirling Cycle
--------------
Suppose that 206 moles of a monatomic ideal gas is initially
contained in a piston with a volume of 1.12 m3 at a temperature of 459 K.
The piston is connected to a hot reservoir with a temperature of 1212 K
and a cold reservoir with a temperature of 459 K.

The gas undergoes a quasi-static Stirling cycle with the following steps:

Step 1.
The temperature of the gas is increased to 1212 K
while maintaining a constant volume.
Step 2.
The volume of the gas is increased to 3.75 m^3
while maintaining a constant temperature.
Step 3.
The temperature of the gas is decreased to 459 K
while maintaining a constant volume.
Step 4.
The volume of the gas is decreased to 1.12 m^3
while maintaining a constant temperature.

a. What is the pressure of the gas under its initial conditions?

Using the ideal gas equation in order to
solve for the pressure of the system

Ideal Gas Law Equation:
    Pressure * Volume = number of moles * R constant * Temperature

Pressure = (number of moles * R constant * Temperature) / Volume

         = 701933.607096 Pa

b. How much energy is transferred into the gas from the hot reservoir?

Step 1:
Changes the temperature of the system to 1212K and maintains volume
so we can use the equation for heatEnergy:

 heatEnergy =
 specific heat constant of volume * number of moles * change in temperature

Step 2:
Volume of the system increases, however the temperature of the system
remains constant.

Work added into the system is defined by:

 Work =
 number of moles * R Constant * Temperature * ln(Volume Final/Volume Initial)

 Add both the heat energy and work that were
 in the system to obtain the value:
 = 4442881.32003

c. How much energy is transferred out of the gas into the cold reservoir?

Step 3:
Changes temperature to 459 K with a constant volume, so we can use step 1's
equation to get:

  heatEnergy =
  specific heat constant of volume * number of moles * change in temperature

Step 4:
Volume of the system increases, however the temperature of the system
remains constant.

Work added into the system is defined by:
 Work =
 number of moles * R Constant * Temperature * ln(Volume Final/Volume Initial)

 Add both energy and work that go into the cold reservoir to get:

      = 2884345.36739


d. How much work is done by the gas during this cycle?

Find the difference in heat in and heat out

Work Done By Gas
    = heat entered - heat exited
    = 1558535.95264 J

e. What is the efficiency of this Stirling cycle?

Efficiency is defined as work done divided by the heat in, which is:

Efficiency Ratio = Work Done by Gas / heatEnergyAdded

                 = 0.350793964632

f. What is the maximum (Carnot) efficiency of a heat engine running between these two reservoirs?

Carnot Efficiency of a heat engine is defined by:

    Carnot Efficiency =
    1 - (Temperature of Cold Reservoir / Temperature of Hot Reservoir)
    = 0.621287128713

"""
import Constants
import math

if __name__ == '__main__':
    n_moles = 206
    initialTemp = 459.0
    initialVolume = 1.12
    secondTemp = 1212.0
    secondVolume = 3.75

    initialPressure = (
        n_moles * Constants.IDEAL_GAS_LAW_CONSTANT *
        initialTemp * (1.0 / initialVolume)
    )

    print "The initial pressure of the system is:", initialPressure

    heatEnergyAfterSecond = (
        Constants.SPECIFIC_HEAT_OF_CONSTANT_VOLUME *
        n_moles * (secondTemp - initialTemp)
    )

    workAfterThird = (
        n_moles * Constants.IDEAL_GAS_LAW_CONSTANT * secondTemp *
        math.log(secondVolume / initialVolume)
    )

    energyAdded = workAfterThird + heatEnergyAfterSecond

    print "The amount of energy added into the system is:", energyAdded

    heatEnergyAfterFourth = (
        Constants.SPECIFIC_HEAT_OF_CONSTANT_VOLUME *
        n_moles * (initialTemp - secondTemp)
    )

    workAfterFifth = (
        n_moles * Constants.IDEAL_GAS_LAW_CONSTANT * initialTemp *
        math.log(initialVolume / secondVolume)
    )

    energySubtracted = -(workAfterFifth + heatEnergyAfterFourth)

    print "The amount of energy leaving the system is:", energySubtracted

    work = energyAdded - energySubtracted

    print "The amount of work done by the gas is:", work

    ratioOfEfficiency = work / energyAdded

    print "The ratio of real efficiency is:", ratioOfEfficiency

    carnotEfficiency = 1 - (initialTemp / secondTemp)

    print "The ratio of Carnot (maximum) efficiency is:", carnotEfficiency
