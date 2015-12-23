# coding=utf-8
"""
Work & PV Diagrams
------------------
An ideal gas contained in a piston can change from State i to State f by three different process,
all of which are depicted in the P vs. V graph shown at the right.
The gas always starts in State i with a pressure of 6.71 × 10 ^ 5 Pa and a volume of 6.6 m^3.
The gas always finishes in State f with a pressure of 3.71 × 10 ^ 5 Pa and a volume of 14.4 m^3.
The three processes used to change the state of the gas from i to f can be a direct,
straight-line path (i > f), a path that goes from i to the intermediate state A to f (i > A > f),
or a path that goes from i to the intermediate state B to f (i > B > f).

The processes i > A and B > f are performed at constant pressure and
the processes i > B and A > f are performed at constant volume.

Given Variables:

v1 = 6.6   v2 = 14.4  p1 = 6.71 * 10 ^ 5   p2 = 3.71 * 10 ^ 5

Questions & Answers:

a. In which process is the most work done by the gas?

   i < A < f since the integral of the PV graph returns the amount of work done by the
   gas, we know that the integral of the PV graph will be greatest with i > A > f

b. How much work is done in the process that changes directly from State i to State f (i > f)?
(In this process, work is done by the gas, so the value of W will be negative.)

  Using the equation:
  deltaW = deltaV * pressure_final
  We know that the area under the curve i < B < F:

  -p1 * (v2 - v1)

  We need to know the triangle amount of area inside of the graph
  in order to solve the total amount of value for triangle

  Calculate the value of the top area:

  -p2 * (v2 - v1) for top

  Find the difference to find the rectangular area and then halve to find triangular area:

  triangle = (-p2 * (v2 - v1)-p1 * (v2 - v1)) * 0.5



c. How much work is done to the system if the process is i > A > F > B > i

  Using the equation:
  deltaW = deltaV * pressure_final

  We know that the area under the curve [work] from i > A > F of gas is:
  -p2 * (v2 - v1)

  We know that the area under the curve [work] from i > B > F of gas is:
  -p1 * (v2 - v1)

  Find difference of Top and Bottom and negate to get...
  Work = -(top - bottom)
       = -2340000

"""

if __name__ == '__main__':

    v1 = 6.6
    v2 = 14.4
    p1 = 6.71 * (10 ** 5)
    p2 = 3.71 * (10 ** 5)

    top = -p2 * (v2 - v1)
    bottom = -p1 * (v2 - v1)
    triangle = (-p2 * (v2 - v1) - p1 * (v2 - v1)) * 0.5
    print "Work by i > F (Triangular Area):", triangle

    workIAfB = -(top - bottom)
    print "Work by i > A > f > B > i is:", workIAfB
