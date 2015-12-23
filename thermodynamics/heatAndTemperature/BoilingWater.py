"""
You wish to boil 1.4 kg of water, which has a specific heat capacity
of 4186 J/kg-K. The water is initially at room temperature (293 K).
Water boils at 373 K.

PART A:
How much energy must be added to the water by heating it in order
for it to start boiling?

In order to solve for the amount of heat energy added into the
ideal gas equation:

Q = mass * capacity of heat * change of temperature
Q = 468832 J


PART B:
Now assume that the water is contained in a 0.2-kg aluminum pot
(cAl = 900 J/kg-K) that is initially at 293 K just like the water.
How much energy must be transferred into the pot-and-water system
in order to raise its temperature to the boiling point of water?

Very similar to the last equation, we wish to increase the energy
of the pot and are asked how much energy would be required in order
to achieve such a task. This is again just plugin and add into
the amount of heat that was required in order to heat the water
to find the total amount of energy required in the Aluminiu and
water system:

373.15 K is the boiling point of water
Q = massOfPot * specificHeatOfAlumminum * ( 373.15 - 293 )
Q = 14427

Total amount of Energy
= 468832 (from last question) + 14427 (from previous equation)
= 483259 J

PART C:
If the water takes 7 minutes to boil in the scenario above,
what is the average power output of the stove burner that the
pot is on? Recall that power is defined as energy per unit time.

Power is defined as Work over Time
Watts is defined as Joules per seconds

So first we must convert minutes to seconds:

totalAmountOfTimeInSeconds
= 7 minutes * 60 seconds
=

Then divide the total amount of energy from last question
over the time we got over 7 minutes in order to find the Power
of the system in Watts:

Power Of System
= totalAmountOfEnergyRequired / totalAmountOfTimeInSeconds
= 1150.61666667

PART D:

Now the aluminum pot is emptied of water and allowed to cool.
Assume that the system consists of the aluminum pot (initial
temperature = 373 K) and the 1 m^3 of air that surrounds it
(initially at 293 K, having mass 1.29 kg and a specific heat
capacity of 1004 J/kg-K.) If we assume the only form of energy
transfer is direct conduction between the aluminum pot and
the still air, at what temperature will this system equilibrate?

So having two different systems in the same environment we can
use the ideal gas equation and the laws of energy conservation
to join both values and solve for a final temperature

0 = (tf(system) - ti(Al)) * mass of Aluminium * specific Heat Of Aluminum +
    (tf(system) - ti(air) * mass of Air * specific Heat of Air

And solve for the tf of the system...

(mass of Aluminium * specific Heat Of Aluminum * ti(Al)) +
 (mass of Aluminium * specific Heat Of Air * ti(Air)) =
  tf(system) (mass of Aluminium * specific Heat Of Aluminum + mass of Air * specific Heat of Air)

  tf(system) =
  [(mass of Aluminium * specific Heat Of Aluminum * ti(Al)) +
  (mass of Aluminium * specific Heat Of Air * ti(Air))] /
  (mass of Aluminium * specific Heat Of Aluminum + mass of Air * specific Heat of Air)
  = 302.761652973 K


"""
if __name__ == '__main__':
    mass = 1.4
    initialTemp = 293
    finalTemp = 373
    specificHeat = 4186

    energyAdded = mass * (finalTemp - initialTemp) * specificHeat

    print "The amount of energy added is:", energyAdded

    massOfPot = 0.2
    specificHeatOfAl = 900.0
    initialTempOfPot = 293.0
    finalTemptOfPot = 373.15

    energyAddedToPot = massOfPot * specificHeatOfAl * (finalTemptOfPot - initialTempOfPot)

    totalAmountOfEnergyNeeded = energyAddedToPot + energyAdded

    print "The amount of energy needed to heat the water and pot system is:", totalAmountOfEnergyNeeded

    totalAmountOfTime = 7 * 60

    powerOfSystemInWatts = totalAmountOfEnergyNeeded / totalAmountOfTime
    print "The power output of the system over a span of 7 minutes is:", powerOfSystemInWatts

    massOfAir = 1.29
    specificHeatOfAir = 1004
    initialTempOfAir = 293
    initialTempOfPot = 373

    finalTemperatureOfAirAndPot = (
        ((massOfPot * specificHeatOfAl * initialTempOfPot) + (massOfAir * specificHeatOfAir * initialTempOfAir)) /
        (massOfPot * specificHeatOfAl + massOfAir * specificHeatOfAir)
    )

    print "The final temperature of the air and pot is:", finalTemperatureOfAirAndPot
