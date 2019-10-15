X: list = [[1, 2],
           [3, 4],
           [1, 1]]

Y: list = [[5, 0, 1],
           [0, 5, 1]]


def multiplication(A: list, B: list) -> list:

    if len(A[0]) != len(B):
        raise Exception("Can't multiply matrixes - size mismatch")

    result: list = []
    for i in range(len(A)):
        row: list = []
        for j in range(len(B[0])):
            row.append(0)
        result.append(row)

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


for row in multiplication(X, Y):
    print(row)

V: list = [1, 3, -5]
Z: list = [4, -3, -1]


def dot_product(A: list, B: list) -> int:

    result: int = 0

    for i in range(len(A)):
        for j in range(len(B)):
            result += A[i] * B[j]

    return result


print(dot_product(V, Z))

