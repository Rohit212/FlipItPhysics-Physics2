"""
A box with a volume of 5.4 L contains 6 molecules. The volume of the box is increased to 12 L.

a. By what factor is the total number of states for all molecules increased?

First we must find the ratio of increment from 12L to 5.4L which is

ratioOfChange
= newVolume / oldVolume
= 2.22222

The number of ways that we can represent a state is defined the by equation:

(A * ohms)^(number of moles or number of molecules)

The value A is represented as the constant value for which any increment of volume
is placed into before being distrbuted to the outside.

Since our volume contains 6 molecules, that is our value of power.
Our ratioOfChange is also defined so we can use the equation to
solve for the rise in the states of molecule representation to get:

increasedStates
= (ratioOfChange * ohms) ^ 6
= (ratioOfChange)^6 (ohms ^ 6)
= 120.427291082

"""
if __name__ == '__main__':
    valueN = 6
    initialVolume = 5.4
    finalVolume = 12

    ratioOfChange = finalVolume / initialVolume

    numberOfNewStates = ratioOfChange ** valueN

    print "The total number of new states is:", numberOfNewStates
