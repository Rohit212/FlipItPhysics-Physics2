# coding=utf-8
"""
Ideal & Real Efficiency
-----------------------
An engine draws energy from a hot reservoir with a temperature of 1250 K
and exhausts energy into a cold reservoir with a temperature of 495 K.
Over the course of one hour, the engine absorbs 1.31 × 10 ^ 5 J from
the hot reservoir and exhausts 7.3 × 10 ^ 4 J into the cold reservoir.

Heat Absorbed:                 1.31 * 10 ^ 5 J
Heat Exhausted:                7.30 * 10 ^ 4 J
Temperature of Hot Reservoir:  1250 K
Temperature of Cold Reservoir: 495  K

a. What is the power output of this engine?

   Change in Work for system is defined by heat change:

   changeInWork = heatAbsorbed - heatExhausted

   Time is defined as 1 hr in statement and has to be transformed to seconds
   1 hour -> 60 minutes -> 3600 seconds

   Power = changeInWork / 3600 seconds

         = 16.1111111111 Watts


b. What is the maximum (Carnot) efficiency of a heat engine
   running between these two reservoirs?

   Carnot Efficiency = 1 - (Heat Exhausted/Heat Absorbed)
   = 0.604

c. What is the actual efficiency of this engine?

   Efficiency =
   1 - (Temperature of Hot Reservoir/Temperature of Cold Reservoir) =
   = 0.442748092

"""
if __name__ == '__main__':
    tH = 1250.0
    tC = 495.0
    absorbQ = 1.31 * (10 ** 5)
    exhaustQ = 7.3 * (10 ** 4)

    work = absorbQ - exhaustQ

    power = work / 3600

    carnotEfficiency = 1 - (tC / tH)

    efficiency = 1 - (exhaustQ / absorbQ)

    print "The power output of the engine is:", power
    print "The maximum (Carnot) efficiency of a heat engine of the two reservoirs is:", carnotEfficiency
    print "The actual efficiency of the heat engine of the two reservoirs is:", efficiency
