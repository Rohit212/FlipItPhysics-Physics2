# coding utf-8
"""
A window air conditioner uses 1300 W of electricity and
has a coefficient of performance of 2.35.

Let's assume that all of that electrical energy is
transformed into work done by the air conditioner to
cool a room with dimensions of 7 m x 7 m x 3 m.

The air inside this room will initially have the same
temperature as the air outside (319 K) and the air
conditioner will attempt to cool the room to 295 K.

For the purposes of estimation, assume that the air
in this room will be cooled at constant volume, that
the specific heat of the air at constant volume is
720 J/kg-K, and that the density of the air is 1.2 kg/m3.

Part A:
How much energy must be transferred out of this room order
to decrease the temperature of the air from 319 K to 295 K?

The amount of energy needed to change the temperature to 295K
from 319K is a simple use of the specific gas law equation.

First we must solve for the mass:
- given volume is 147 meters cubed
- multiply the density of air by volume cubed to get mass

Change in temperature is the simple:
- TempDifference = 295K - 319K

Specific Heat of Air with Constant Volume is:
- 720 J/kg-K

Our Answer should be a positive Q since we care only of the
positive value relative to Q

Q = m * C * (Tf - Ti)
  = volume(cubed) * density * tempDifference * specificHeatOfAir * -1
  = 3048192.0

Part B:
How much work will be done by the air conditioner during
the process of cooling the room?

Since we are given the Coefficient of Realistic Performance,
we know we can use the equation:

Coefficient of Realistic Performance for a Refrigerator (heat flows out)
= heat of cold reservoir / work on engine

Solving for the Work to get

Work
= heatOfColdReservoir / Coefficient Of Realistic Performance
= 1297102.97872 J

Part C:
How much time in minutes will it take for the room to
cool using this air conditioner?

Power = Work / Time
Solve for Time
Time = Work / Power

Assuming the power of the motor is 1300 Watts, we need to change
the units to minutes.

1300 Watts = 1300 J / S = 1300 * 60 J / Minute

Using the new units we have need to obtain the amount of work
needed, which is simply the calculated amount of work from Part B

From Part B: 1297102.97872 J

Solve all variables to find the solution is:

Time
= 1297102.97872 J / 1300 * 60
= 16.6295253682 minutes

Part D:
How much time in minutes would the cooling process take
if instead we used an air conditioner that uses a Carnot
cycle that operates between 319 K and 295 K?

First we find the coefficient of Carnot Performance

Coefficient of Maximum (Carnot) Performance of a Refrigerator
= 1 / ([temperature of heat reservoir / temperature of cold reservoir] - 1)
= Coefficient of Carnot Performance

Using the Coefficient Carnot Performance to get the value of work

Coefficient of Carnot Performance
= heat of cold reservoir / work on engine

workOnEngine = heatOfColdReservoir / coefficientOfCannotPerformance

Using the same equation from Part C:
Time = Work / Power

Time = workOnEngine / (1300 * 60)


"""
if __name__ == '__main__':
    airConditionPower = 1300
    coefficientOfPerformance = 2.35
    volumeOfRoom = 7 * 7 * 3

    initialTempOfRoom = 319.0
    finalTempOfRoom = 295.0
    temperatureDifference = 295 - 319

    specificHeatOfAirAtConstantVolume = 720
    densityOfAir = 1.2  # kg/meters cubed

    HeatNeededAtConstantVolume = (
        volumeOfRoom * densityOfAir * temperatureDifference *
        specificHeatOfAirAtConstantVolume * -1
    )

    print "The amount of energy needed to decrease the temperature is:", HeatNeededAtConstantVolume

    workDoneByAir = HeatNeededAtConstantVolume / coefficientOfPerformance

    print "The amount of work done by the air conditioner is:", workDoneByAir

    powerByMinute = airConditionPower * 60
    timeForRealistic = workDoneByAir / powerByMinute

    print "It will take about", timeForRealistic, "minutes"

    coefficientOfCarnotPerformance = (
        1 / ((initialTempOfRoom / finalTempOfRoom) - 1)
    )

    workDoneByAir = HeatNeededAtConstantVolume / coefficientOfCarnotPerformance
    timeForCarnot = workDoneByAir / powerByMinute

    print "Using an air conditioner that uses the Carnot Cycle would take", timeForCarnot, "minutes"
