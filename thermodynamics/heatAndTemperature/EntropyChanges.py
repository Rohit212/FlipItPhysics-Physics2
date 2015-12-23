"""
A physics textbook is pushed across the tabletop with a force
of 259 N over a distance of 2.3 m. The book slides across the
table and comes to a stop. The temperature of the entire system
(defined as the table, the book, and the surrounding air) is 295 K.

Part A:
What is the change in the internal energy of the system?

The amount of work done on the system is equal to
Work = Force * Distance

We know then that the amount of work added to the internal energy
of the system is:

Internal Energy
= force * distance
= 2.3 * 259
= 595.7 J

Part B:
Assuming that the temperature of the system does not
significantly change during this process, what is the
change in the entropy of this system?

In order to understand the next question we must be able to
understand that no significant change is occurring in the temperature
of the system. Meaning that the temperature of 295K will remain
consistent and a determining factor for the energy in the system.

Basically, we can use it as a ratio to compare the amount
of chaos that occurred in our system, which is the
ratio of internal energy change and the amount of temperature
that occurred initially:

ratioOfChange
= internalEnergyChange / temperatureInitial
= 2.0193220339

You can also see that the answer units are Joules per Kelvin
and the only energy we have is the change in energy
from the first equation and the initial temperature in Kelvin

"""

if __name__ == '__main__':
    force = 259
    distance = 2.3
    initialTemperature = 295

    work = force * distance

    print "The total change in the amount of energy located in the system is:", work

    ratioOfChange = work / initialTemperature

    print "The change in entropy of the system is:", ratioOfChange
