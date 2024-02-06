def diagonally_dominant(Aaug):

    """
    Makes a matrix diagonally dominant

    :param Aaug: (list of lists) An augmented matrix [A | b] with N rows and N+1 columns.

    :return: A diagonally dominant augmented matrix.
    """

    N = len(Aaug)
    for i in range(N):
        max_value = abs(Aaug[i][i])
        max_index = i
        for j in range(i + 1, N):  # Finds the max number of the column
            if abs(Aaug[j][i]) > max_value:
                max_value = abs(Aaug[j][i])
                max_index = j
        if i != max_index:  # Swaps rows if needed to make the matrix diagonally dominant
            Aaug[i], Aaug[max_index] = Aaug[max_index], Aaug[i]


def GaussSeidel(Aaug, x, Niter=50):
    """

    :param Aaug: (list of lists) An augmented matrix [A | b] with N rows and N+1 columns.
    :param x: (list) The initial guess for the solution.
    :param Niter: (int) The number of iterations to perform.

    :return:The final solution vector.
    :rtype: list
    """
    diagonally_dominant(Aaug)  # Runs to make sure function is diagonally dominant

    A = [row[:-1] for row in Aaug]  # A is all the columns except the last one
    b = [row[-1] for row in Aaug]  # b is only the last column

    N = len(b)

    # Performs Gauss-Seidel iteration
    for _ in range(Niter):

        for j in range(N):
            summation = sum(A[j][k] * x[k] for k in range(N) if k != j)
            x[j] = (b[j] - summation) / A[j][j]

    return x


def main():
    # Example 1
    Aaug1 = [[3, 1, -1, 2],
             [1, 4, 1, 12],
             [2, 1, 2, 10]]

    xo1 = [0, 0, 0]
    result1 = GaussSeidel(Aaug1, xo1)
    print("Example 1 Result:", result1)

    # Example 2
    Aaug2 = [[1, -10, 2, 4, 2],
             [3, 1, 4, 12, 12],
             [9, 2, 3, 4, 21],
             [-1, 2, 7, 3, 37]]
    xo2 = [0, 0, 0, 0]
    result2 = GaussSeidel(Aaug2, xo2)
    print("Example 2 Result:", result2)


main()
