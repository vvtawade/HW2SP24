import math


def PDF(args):

    """
    Function that performs the Gaussian/normal probability density formula (PDF)

    :param args: (tuple) Tuple which contains x, mu, sigma (x, population mean, population standard deviation).

    :return: Value for the Gaussian/normal probability density function
    :rtype: float
    """

    x, mu, sigma = args  # x, mu (population mean), sigma (population standard deviation)
    # Gaussian/normal probability density function
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * (((x - mu) / sigma)**2))


def Probability(PDF, args, c, GT=True):

    """
    Calculates the probability of x using Simpson's 1/3 integration rule and the Gaussian/normal probability density
        function

    :param PDF: (function) The callback function for the Gaussian/normal probability density function.
    :param args: (tuple) Tuple which contains mu and sigma (population mean and population standard deviation).
    :param c: (float) The upper limit of integration.
    :param GT: (bool) Indicates whether x>c (GT=True) or x<c (GT=False).

    :return: The probability value.
    :rtype: float
    """

    n = 1000  # num of sub-intervals
    result = 0.0
    mu, sigma = args  # Tuple, args, containing mu and sigma

    if GT:  # (x>c)
        x = mu - (5 * sigma)
    else:  # (x<c)
        x = mu + (5 * sigma)

    h = (c - x) / n  # Calculation of h in Simpson’s 1/3 rule

    result = PDF((x, mu, sigma))  # Calculates initial point of probability density
    for i in range(1, n):
        xi = x + i * h  # Calculates midpoint of intervals
        coef = 4 if i % 2 == 1 else 2  # Alternates coefficient between 4 and 2 as per Simpson's Rule
        result += coef * PDF((xi, mu, sigma))  # Evaluates PDF and summation (integration)

    result += PDF((c, mu, sigma))

    result *= h / 3  # Multiplies summation of intervals by h / 3

    return result


def main():

    # First example
    args1 = (100, 12.5)  # (mu, sigma)
    c1 = 105
    result1 = Probability(PDF, args1, c1, GT=False)  # Returns Probability function as result1
    print(f'P(x<{c1:.2f}|N({args1[0]}, {args1[1]})) = {result1:.2f}')  # Prints result1

    # Second example
    args2 = (100, 3)
    c2 = args2[0] + 2 * args2[1]
    result2 = Probability(PDF, args2, c2, GT=True)
    print(f'P(x<{c1:.2f}|N({args2[0]}, {args2[1]})) = {result2:.2f}')


main()





