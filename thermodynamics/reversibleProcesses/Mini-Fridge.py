# coding=utf-8
"""
A mini-fridge needs to maintain a temperature of 277 K.
The air outside the mini-fridge has a temperature of 292 K.

Every fifteen minutes 3.25 × 10^5 J of energy is transferred
out of the mini-fridge and 4.06 × 10^5 J of energy is transferred
into the surrounding air.

a. What is the power output (that is, the work done per second)
   of the compressor in the mini-fridge?

Power is defined as Work / Time
Watts are defined as joules per second

We can find the difference of values in both the amount of energy
placed into the surrounding air and the energy subtracted from
the entire fridge system to get work.

Work on System = Energy Transferred In - Energy Transferred Out
Except that this amount of work only occurs every 15 minutes

Converting 15 minutes to seconds is...
15 minutes -> 900 seconds

We then divide our Work from Time to get:

= 90.0 Watts

b. What is the coefficient of performance of this mini-fridge?

The coefficient of performance given only temperature requires the use
Coefficient of Realistic Performance:

Coefficient of Performance for a Refrigerator (heat flows out)
= 1 / ([heat of hot reservoir / heat of cold reservoir] - 1)

Note, we use the given energy values and even though they are not
the energy of the system, the ratio is sufficient enough to obtain
an answer

After plugging in, the answer is...
= 4.01234567901

c. If this mini-fridge were instead cooled by a Carnot engine
   used as a refrigerator, what would its coefficient of performance be?

Question asks us to use Coefficient of Maximum (Carnot) Performance
Calculation for the question, which is:

Coefficient of Maximum (Carnot) Performance of a Refrigerator
= 1 / ([temperature of heat reservoir / temperature of cold reservoir] - 1)

After plugging in, the answer is...
= 18.4666666667

d. If the mini-fridge were cooled by a Carnot engine, how much
   energy would be transferred out of the mini-fridge every
   fifteen minutes if the power output of the compressor
   was the same as above?

   Assume that our required Power is 90 Watts.
   Solving for the temperature of cold reservoir

   We need to be able to produce the same amount of work in order
   to maintain the level of power in the system

   Coefficient of Realistic Performance for a Refrigerator (heat flows out)
   = heat of cold reservoir / work by engine

   Simplify and solve for heat of Cold Reservoir using the Carnot's COP:

   heatOfColdReservoir = work by engine * Coefficient Of Carnot's Performance

   solve to get:
   = 1662 J
   Which is the amount of energy added every minute.
   We need the energy every 15 minutes so...

   = heatOfColdReservoir * 15 * 60
   = 1495800 J
"""
if __name__ == '__main__':
    hotTemperature = 292.0
    coldTemperature = 277.0
    outOfFridgeEveryFifteenMinutes = 3.25 * (10 ** 5)
    intoAirEveryFifteenMinutes = 4.06 * (10 ** 5)

    workOfSystem = intoAirEveryFifteenMinutes - outOfFridgeEveryFifteenMinutes

    powerOfSystem = workOfSystem / 900

    print "The power output of the system is:", powerOfSystem

    realCoefficientPerformance = 1.0 / ((intoAirEveryFifteenMinutes / outOfFridgeEveryFifteenMinutes) - 1)

    print "The Real Coefficient of Performance is:", realCoefficientPerformance

    carnotCoefficientPerformance = 1.0 / ((hotTemperature / coldTemperature) - 1)

    print "The Carnot Coefficient of Performance is:", carnotCoefficientPerformance

    heatOutUsingCarnotEngine = powerOfSystem * carnotCoefficientPerformance

    heatOutUsingCarnotEngine = heatOutUsingCarnotEngine * 60 * 15

    print "The total amount of heat used in 15 minutes is:", heatOutUsingCarnotEngine
