from typing import List

def lcs(X: str, Y: str) -> int:
    m = len(X)
    n = len(Y)

    # Create (m+1) x (n+1) matrix initialized to 0
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    print(f"X = {X}")
    print(f"Y = {Y}")

    print("\nInitial row:")
    print(c[0])

    # Build the LCS matrix
    for i in range(1, m + 1):

        for j in range(1, n + 1):

            # Case 2: Characters match
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1

            # Case 3: Characters do not match
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]

            else:
                c[i][j] = c[i][j - 1]

        # Print row after it has been completed
        print(f"Row {i} ({X[i - 1]}): {c[i]}")

    # Print final matrix
    print("\nFinal LCS Matrix:")

    print("    ", end="")
    for char in Y:
        print(f"{char:3}", end="")
    print()

    for i in range(m + 1):

        if i == 0:
            print("  ", end="")
        else:
            print(f"{X[i - 1]} ", end="")

        for value in c[i]:
            print(f"{value:3}", end="")

        print()

    # Bottom-right cell contains the LCS length
    print(f"\nLCS Length = {c[m][n]}")

    return c[m][n]
