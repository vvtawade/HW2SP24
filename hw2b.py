import math


def Secant(fcn, x0, x1, maxiter, xtol):

    """
    A function that finds the root of an equation using the Secant Rule equation.

    :param fcn: (function) The function that finds the root.
    :param x0: (float) The initial guess for the root.
    :param x1: (float) The current guess for the root.
    :param maxiter: (int) The number of iterations.
    :param xtol: (int) The tolerance for convergence.

    :return: The root to the equation
    :rtype: float

    """

    x_previous = x0  # Initial secant line intersection
    x_current = x1  # Second secant line intersection

    for i in range(maxiter):
        x_next = x_current - (fcn(x_current) * ((x_current - x_previous) / (fcn(x_current) - fcn(x_previous))))
        # Secant Rule Equation

        if abs(x_current - x_previous) < xtol:  # Returns solution when difference of x values is below tolerance
            return x_next

        x_previous = x_current  # Replaces prior x value with current
        x_current = x_next  # Replaces current x value with next value obtained from equation

    return x_current  # Returns current x value if maxiter is reached


def main():
    def fcn1(x):
        return x - 3 * math.cos(x)  # Function 1

    def fcn2(x):
        return math.cos(2 * x) * x ** 3  # Function 2

    answer1 = Secant(fcn1, x0=1, x1=2, maxiter=5, xtol=1e-4)  # Callback to Secant() function
    answer2 = Secant(fcn2, x0=1, x1=2, maxiter=15, xtol=1e-8)
    answer3 = Secant(fcn2, x0=1, x1=2, maxiter=3, xtol=1e-8)
    print('The root to function 1 is: {:.5f}'.format(answer1))  # Prints root1
    print('The root to function 2 is: {:.5f}'.format(answer2))  # Prints root2
    print('The root to function 2 is: {:.5f}'.format(answer3))  # Prints root2


main()
