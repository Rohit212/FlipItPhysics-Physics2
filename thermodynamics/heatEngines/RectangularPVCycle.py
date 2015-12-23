# coding=utf-8
"""
Rectangular PV Cycle
--------------------
A piston contains 170 moles of an ideal monatomic gas that initially
has a pressure of 2.06 × 10^5 Pa and a volume of 1.7 m^3.
The piston is connected to a hot and cold reservoir and the gas
goes through the following quasi-static cycle accepting energy from the
hot reservoir and exhausting energy into the cold reservoir.

Steps:
- The pressure of the gas is increased to 5.06 × 10^5 Pa
  while maintaining a constant volume

- The volume of the gas is increased to 8.7 m^3
  while maintaining a constant pressure

- The pressure of the gas is decreased to 2.06 × 10^ 5 Pa
  while maintaining a constant volume

- The volume of the gas is decreased to 1.7 m ^ 3 while
  maintaining a constant pressure

Recall that:
- an ideal gas with constant volume has a specific heat of 12.47 J/K * mole
- an ideal gas with constant pressure has a specific heat of 20.79 J/K * mole
- the number of gas molecules is equal to Avogadro's Number
  6.022 * 10^23 times the number of moles of the gas

a. How much energy is transferred into the gas from the hot reservoir?

Step 1 transfers heat to the system so we can use the
Constant Volume Equation of:

heatEnergy =
  specific heat constant of volume * initial Volume *
  (final pressure - initial pressure) / R constant

Step 2 requires another additional heat source
in order to maintain the pressure at a constant
as the volume expands. We use the system of:

heatEnergy =
   specific heat constant of pressure * pressure *
   (final volume - initial volume) * (1.0 / R constant)

Combining both of these energies produces the total
heat energy entering the system

           = 9621534.14136


b. How much energy is transferred out of the gas into the cold reservoir?

From the last problem we know that a certain amount of heat entered the
reservoir. The next two energy processes lead to a decrement in the
heat of the system and eventually produce the amount of heat
actually lost in the system. We basically do the same as last
question but just move in reverse.

Step 3 requires a reduction of heat from the system
by maintaining a constant volume while reducing the pressure
of the system and transferring energy to the reservoir

heatEnergy =
   specific heat constant of volume * secondVolume *
   (final pressure - initial pressure) / R constant

Step 4 requires a reduction in volume while maintaing a cosntant
pressure and transferring energy to cold reservoir

heatEnergy =
   specific heat constant of pressure * pressure *
   (final volume - initial volume) * (1.0 / R constant)

Add both negative values from step 3 & 4, then negate since it only
asks for the amount of energy that has moved

           = 7520135.39782

c. How much work is done by the gas?

The amount of work done by the gas is the difference between
both the amount of heat added to the system and subtracted
the amount of heat that has left the system.

Work Done By Gas
    = heat entered - heat exited
    = 2101398.74354 J

d. What is the efficiency of this cycle?

Efficiency of a cycle is defined by the amount of work
done the gas divided by the total amount of energy that
has entered the system to create a ratio of Work/Heat Added.

Efficiency = Work / (Heat Added)
           = 2101398.74354 / 9621534.14136
           = 0.218405787753
"""
import Constants

if __name__ == '__main__':
    number_of_moles = 170
    initialPressure = 2.06 * (10 ** 5)
    initialVolume = 1.7
    secondPressure = 5.06 * (10 ** 5)
    secondVolume = 8.7
    thirdPressure = 2.06 * (10 ** 5)
    thirdVolume = 1.7

    heatEnergyAfterSecond = (
        Constants.SPECIFIC_HEAT_OF_CONSTANT_VOLUME *
        initialVolume * (secondPressure - initialPressure) *
        (1.0 / Constants.IDEAL_GAS_LAW_CONSTANT)
    )
    heatEnergyAfterThird = (
        Constants.SPECIFIC_HEAT_OF_CONSTANT_PRESSURE *
        secondPressure * (secondVolume - initialVolume) *
        (1.0 / Constants.IDEAL_GAS_LAW_CONSTANT)
    )
    heatEnergyAdded = heatEnergyAfterSecond + heatEnergyAfterThird
    print "The total amount of energy added into the system by the hot reservoir is:", heatEnergyAdded

    heatEnergyAfterFourth = (
        Constants.SPECIFIC_HEAT_OF_CONSTANT_VOLUME *
        secondVolume * (initialPressure - secondPressure) *
        (1.0 / Constants.IDEAL_GAS_LAW_CONSTANT)
    )
    heatEnergyAfterFifth = (
        Constants.SPECIFIC_HEAT_OF_CONSTANT_PRESSURE *
        initialPressure * (initialVolume - secondVolume) *
        (1.0 / Constants.IDEAL_GAS_LAW_CONSTANT)
    )

    heatEnergySubtracted = -(heatEnergyAfterFourth + heatEnergyAfterFifth)
    print "The total amount of energy subtracted from the system by cold reservoir is:", heatEnergySubtracted

    work = heatEnergyAdded - heatEnergySubtracted

    print "The total amount of work done by the gas is:", work

    ratioOfEfficiency = work / heatEnergyAdded

    print "The ratio of real efficiency is:", ratioOfEfficiency
