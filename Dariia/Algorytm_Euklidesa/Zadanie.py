def iteracja(a, b):
    r = 0
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def rekurencja(a, b):
    if b > 0:
        r = a % b
        a = b
        b = r
        return rekurencja(a, b)
    if b <= 0:
        return a


if __name__ == '__main__':
    print(iteracja(49, 84))
    print(rekurencja(49, 84))
