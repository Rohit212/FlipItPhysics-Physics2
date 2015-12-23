"""
A heat pump uses an ideal Carnot cycle to heat a house.
The outside air has a temperature of 294 K and the house is kept
at a temperature of 304 K.

a. What is the coefficient of performance of this heat pump?

We can use the equation for Coefficient Performance of a Heat Pump:

Coefficient of Maximum (Carnot) Performance for a Heat Pump
= 1 / (1 - [temperature of cold reservoir / temperature of hot reservoir])

= 30.4

b. If the heat pump does 1400 J of work on the working substance,
   how much energy is transferred into the house?

The question wants the amount of heat that has been inserted into the heat
reservoir. We can solve for the heat of hot reservoir using the equation:

Coefficient of Performance for a Heat Pump (heat flows in)
= heat of hot reservoir / work on engine

heatOfHotReservoir
= Coefficient of Performance for Heat Pump * work on Engine
= 42560 J

c. In the scenario described in the previous question,
   how much energy is transferred out of the outside air?

If we're focusing on the amount of energy flowing in to the air
then we can understand that the amount of energy from the fridge
is the amount of initial heat inside the system subtracted by
any of the work done by the system.

EnergyToAir
= heatOfHotReservoir - workDoneBySystem
= 41660 J

"""
if __name__ == '__main__':
    highHeat = 304.0
    lowHeat = 294.0
    carnotCoefficientPerformance = 1.0 / (1.0 - (lowHeat / highHeat))

    print "The Carnot Coefficient Performance for the Heat Pump is:", carnotCoefficientPerformance

    workDoneOnSystem = 1400

    heatAddedTfReservoir = carnotCoefficientPerformance * workDoneOnSystem

    print "The amount of heatAdded transferred to the house is:", heatAddedTfReservoir

    totalEnergyToHouse = heatAddedTfReservoir - workDoneOnSystem

    print "The amount of energy transferred into the air is:", totalEnergyToHouse
