"""
A block with a mass of 4.4 kg is dropped from rest from a
height of 4.9 m, and remains at rest after hitting the ground.

Part A:
If we consider the system to consist of the block, the ground,
and the surrounding air, what is the change in the
internal energy of the system?

Assuming that all of the kinetic energy transforms into
internal energy the second it touches the ground, we can
assume that the potential energy at said height transforms
into internal energy the second it hits the ground.

Potential Energy Equation with Height:

Potential Energy = mass * height * constant of Gravity on earth

= 211.5036 J

Part B:
Which of the following phenomena would NOT happen due to
the change in the internal energy of the system?

- The molecules of the block vibrate faster
- The molecules of the ground vibrate faster.
- The surrounding air molecules move faster.
- The sound of the block hitting the ground travels through the air.
- All of these phenomena would happen.

We know that if all of the potential energy transforms into
internal energy, then all of the resulting factors that occurred
by block falling are transferred into internal energy. Therefore,
the internal energy is a combination of all of the listed phenomena.

Answer =

All of these phenomena would happen.

"""
if __name__ == '__main__':
    massOfBlock = 4.4
    heightOfBlock = 4.9
    constantOfGravity = 9.81

    PotentialEnergy = massOfBlock * heightOfBlock * constantOfGravity

    print "The amount of energy converted into internal energy is:", PotentialEnergy

    option = "All of these phenomena would happen."

    print "The option:", option
