"""
A block with a mass of m1 = 1.8 kg is pushed to the right with
a force of 602 N for a distance of 2.4 m across a horizontal
frictionless surface, after which the force is removed.

The 1.8-kg block then collides with a second block with
a mass m2 = 7.3 kg, which is initially at rest.
The two blocks stick together after the collision.

Part A:
Determine the change in the internal energy of the
system of blocks during the collision.

Knowing that momentum stays constant, we can use it to hypothesis
our initial and final momentum of our system and then use the
difference in velocities

First we must solve for the final velocity of Block A

The amount of work done on Block A is...
Equation for Work:
Work = Force x Distance

Block A's Force is 602N with a travel distance of 2.4m which is
a total work of
Work of A =
602N * 2.4m
= 1444.8 J

Using the kinetic energy formula we can solve for the velocity
of block A during collision

kineticEnergy = 1/2(mass * velocity^2)

Work of A = 1/2 (mass * velocity^2)

velocityOfA
= sqrt(2*workOfA/massOfBlockA)
= 40.06 m/s

taking velocity A into account we can use the momentum stays constant to get:

mass of block A * velocity of block A = (massOfBlockA + massOfBlockB) * finalVelocity
and solve for the finalVelocity to get:

finalVelocity = massOfBlockA * velocityOfBlockA / (massOfBlockA + massOfBlockB)

and then find the kinetic energy differences using the kinetic energy formula for both
beginning and ending values

kineticEnergyBeginning = 1444.8J

kineticEnergyFinal = 1/2(massOfBlockA + massofBlockB) * velocityFinal ^ 2

totalKineticEnergyChange
= kineticEnergyBeginning - kineticEnergyFinal
= 1159 J

Part B:
Now assume that the 7.3-kg block is traveling at 7.5 m/s to the left
before the collision. The two blocks will still stick together after
the collision. Determine the change in the internal energy of the
system of blocks.

Similar to the last question, we must solve for both of the system's but
find a completely new finalVelocity since block B now has an initial momentum
going to the left.

From the previous question we know that our initial velocity of block A is:

velocityOfA
= 40.06 m/s

Let's solve for the final velocity by using the momentum equations

massOfBlockA * velocityOfBlockA + massOfBlockB * velocityofBlockB
= finalVelocity(massOfBlockB + massOfBlockA)

We can rewrite the equation to get:

finalVelocity =

(massOfBlockA * velocityOfBlockA + massOfBlockB * velocityOfBlockB) / (massOfBlock A + massOfBlockB)

= 1.90878023806 m/s

We must also solve for initial kinetic energy of blockB
since it now has a velocity:

initialKineticEnergyOfBlockB
= 1/2(massOfBlockB * velocityOfBlockB^2)
=

Let's sum up the initial kinetic energies to get:

totalInitialKineticEnergy
= initialKineticEnergyOfBlockB + initialKineticEnergyOfBlockA
=

Again we just plugin our final kineticEnergy using our final velocity to get:

kineticEnergyFinal
= 1/2(massOfBlockA + massOfBlockB)finalVelocity^2
=

and then find the kineticEnergyChange by simply subtracting the kineticEnergies

kineticEnergyChange
= totalInitialKineticEnergy - kineticEnergyFinal
= 1633.53483 J

woo, that was a pretty tedious question

"""
import math

if __name__ == '__main__':
    massOfBlockA = 1.8
    massOfBlockB = 7.3
    forceOnBlockA = 602
    distanceByBlockA = 2.4

    workDoneOnBlockA = forceOnBlockA * distanceByBlockA
    velocityOfA = math.sqrt(2 * workDoneOnBlockA / massOfBlockA)

    finalVelocity = velocityOfA * massOfBlockA / (massOfBlockA + massOfBlockB)

    kineticEnergyFinal = 0.5 * (massOfBlockB + massOfBlockA) * (finalVelocity ** 2)

    totalKineticEnergyChange = workDoneOnBlockA - kineticEnergyFinal

    print "The total internal energy change is:", totalKineticEnergyChange

    velocityOfBlockB = -7.5

    finalVelocity = (massOfBlockA * velocityOfA + massOfBlockB * velocityOfBlockB) / (massOfBlockB + massOfBlockA)

    initialKineticEnergyOfB = 0.5 * massOfBlockB * velocityOfBlockB ** 2

    totalInitialKineticEnergy = initialKineticEnergyOfB + workDoneOnBlockA

    kineticEnergyFinal = 0.5 * (massOfBlockA + massOfBlockB) * finalVelocity ** 2

    kineticEnergyChange = totalInitialKineticEnergy - kineticEnergyFinal

    print "The total internal energy change is:", kineticEnergyChange