# coding=  utf-8
"""
A tank with constant volume of 2.19 m^3 contains 13.5 moles of
a monatomic ideal gas. The gas is initially at a temperature of
300K. An electric heater is used to transfer 50600 J of energy into
the gas.

PART A:
What is the temperature of the gas after the energy is added?

Using the specific heat formula and specific heat
constant existent with constant volume we can solve
for the final temperature of the gas.


Q = specificHeatConstantOfVolume * (tempFinal - tempInitial) * numberOfMoles

tempFinal
= Q/(specificHeatConstantOfVolume * numberOfMoles) + tempInitial
= 600.573227598 K

PART B:
What is the change in pressure of the gas?

In order to solve for the difference in pressure we must use
the equation:

pressure * volume = number of moles * R constant * temperature

We must find both the initial and final pressure, and then
find the difference between both values in order to solve the question

We can use the formulas from Boyle's Law:

pressure final / temperature final = pressure initial / temperature initial

pressure final = temperature final * (pressure initial / temperature initial)

so now we need to solve for the initial pressure...

pressure initial * volume initial = temperature initial * n moles * R constant
pressure initial = temperature initial * n moles * R constant / volume initial

We know the rest of the equations and can simple solve them now
pressure difference
= pressure final - pressure initial
= 15405.4398026 Pa



PART C:
How much work was done by the gas during this process?

We know that the equation for finding out
whether or not the gas in any system has done work is:

change in work = change in volume * -(final pressure)

Since no change in volume occurred in the system, we
know that no work was done by the gas.

Work done by gas
= 0
"""
import Constant
if __name__ == '__main__':
    n_moles = 13.5
    tempInitial = 300
    heatEnergy = 50600
    volInitial = 2.19

    tempFinal = tempInitial + (heatEnergy / (Constant.SPECIFIC_HEAT_OF_CONSTANT_VOLUME * n_moles))
    print tempFinal

    presInitial = n_moles * tempInitial * Constant.R / volInitial

    presFinal = tempFinal * (presInitial / tempInitial)

    presDifference = presFinal - presInitial

    print "The change in pressure of the gas is:", presDifference

    print "The gas has done zero work since the volume has not changed."

