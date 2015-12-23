# coding=utf-8
"""
A container contains 133 moles of Gas A and 115 moles
of Gas B separated by a movable airtight divider.

Part A:
Initially, we will assume that the container is cylindrical.
If the cylinder is 2.2 m long, how far from the left side of
the cylinder will we find the equilibrium position of the divider?

Assuming that the cylinder doesn't change, we can just
find the average of the molecules and multiple it by
the length of cylinder to find the cutoff point.

totalMole
= numberOfMolesA numberOfMOlesB

gasA is located on the left, so we use it for the average:

ratioOfAverages
= numberOfMoleculesA / totalMole


and then multiple it by the height to get:

locationOfDivider
= ratioOfAverages * height
= 1.17983870968 meters from left

Part B:
Now assume that this container is shaped like a cone, as shown on the right.
The cone has a height of 2.2 m and the tip of the cone makes an angle of 90°.
At what distance from the tip of the cone will we find the equilibrium
position of the divider?

Remember that the volume of a cone is given by  π*r^2)h/3, where h is the height
and r is the radius of the base.

Again, gas A is located to the left.
Since the tip of the angle is at 90 degrees and this is a cone,
the radius and the height of the cone are constantly equal to each other.

Knowing this fact we can rewrite the equation to:

= pi * radius ^ 2 * height / 3
= pi * height ^ 3 / 3

And we're solving for the point at which the volume is at
the ratioOfAverages from the last question.

so we can solve for value of volume at which we want our solution
to be at by doing:

volumeWanted
= ratioOfAverages * pi * (max_height) ^ 3 / 3
= 5.97976 meters cubed

Now we need to solve for the height or radius to get...

heightNeeded
= cubedRoot(3 * volumeWanted/ pi)
= 1.78740376144 meters from the left side

"""
if __name__ == '__main__':
    cylinderHeight = 2.2
    numberOfMolesA = 133.0
    numberOfMolesB = 115.0
    totalMole = numberOfMolesA + numberOfMolesB

    ratioOfAverages = numberOfMolesA / totalMole

    locationOfDivider = ratioOfAverages * cylinderHeight

    print "The location of the divider for the cylinder starting from the left is:", locationOfDivider

    PI = 3.1415

    volumeWanted = PI * (cylinderHeight ** 3) * ratioOfAverages / 3.0

    heightNeeded = (3 * volumeWanted / PI) ** (1.0 / 3.0)

    print "The location of the divider for the cone starting from the left is", heightNeeded
