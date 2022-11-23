n = int(input("Write a number [1000,9999]: "))


def reachable_number(num: int) -> int:
    if int(num / 1000) != 0:
        for k in range(1, num):
            k1 = int(k / 1000)
            k2 = int(k % 1000 / 100)
            k3 = k % 100 / 10
            k4 = k % 10
            if k + (int(k1) + int(k2) + int(k3) + k4) == num:
                return num


if reachable_number(int(n)) is None:
        print(n, "- nie jest osiągalna")
else:
    print(reachable_number(int(n)), "jest osiągalna")

for i in range(1000, 9999):
    if reachable_number(int(i)) is None:
        print(i, "nie jest osiągalna")
    else:
        print(str(reachable_number(int(i))), "jest osiągalna")

input()
