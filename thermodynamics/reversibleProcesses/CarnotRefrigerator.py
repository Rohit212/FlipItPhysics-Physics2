"""
A refrigerator uses an ideal Carnot cycle to cool its interior.
The outside air has a temperature of 304 K and the refrigerator
is kept at a temperature of 279 K.

a. What is the coefficient of performance of this refrigerator?

Equation for coefficient of performance for a refrigerator is:

= 1 / ([temperature of hot reservoir / temperature of cold reservoir] - 1)

Plugging in the given temperatures we obtain the value:

= 11.16, the coefficient of maximum performance for refrigerator

b. If the refrigerator does 1400 J of work on the working substance,
   how much energy is transferred out of the refrigerator's interior?

The amount of work done in a system is defined by the difference of the
energy that enters and exits the system.

Our previous question provided us the coefficient ratio with which we can
use to solve for the heat of cold reservoir.

Assuming that 1400J of work entered the system as the energy of the
heat reservoir, we use the Coefficient of Performance for a Refrigerator
equation to solve for heat leaving to the cold reservoir

workOfFridge = 1400 J

Equation:
Coefficient of Performance for a Refrigerator
= heatOfColdReservoir / workOnEngine

Coefficient of Performance for a Refrigerator * workOnEngine
= heatOfColdReservoir
= 15624.0 J

c. In the scenario described in the previous question,
   how much energy is transferred into the outside air?

With the added amount of work, we can establish the amount of joules
leaving the system. In addition, we also have the heat from
work produced by the engine:

EnergyToAir
= workOnEngine + heatOfColdReservoir
= 15624.0 J
"""

if __name__ == '__main__':
    hotTemperature = 304.0
    coldTemperature = 279.0

    CarnotCoefficientPerformance = 1.0 / (hotTemperature / coldTemperature - 1)
    print "The coefficient of performance for the refrigerator is:", CarnotCoefficientPerformance

    workDoneByFridge = 1400

    energyTransferredOutOfFridge = CarnotCoefficientPerformance * workDoneByFridge

    print "The amount of energy transferred out of the fridges interior is", energyTransferredOutOfFridge

    totalEnergyToAir = energyTransferredOutOfFridge + workDoneByFridge

    print "The amount of energy transferred into the air is:", totalEnergyToAir
