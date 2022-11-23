from functools import reduce


def fact2(n: int):
    return reduce(int.__mul__, range(n, 0, -2), 1)


def fact(n: int):
    return reduce(int.__mul__, range(n, 0, -1), 1)


def calculate_pi(n: int) -> float:

    return 2 * sum([
        fact(k) / fact2(2*k + 1) for k in range(n+1)
    ])


print(calculate_pi(10))
