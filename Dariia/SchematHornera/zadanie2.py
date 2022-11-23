n = int(input("Write down number of cofficient : "))
a = []
for i in range (n):
    a.append(int(input(f"{i} number - ")))
X = 2


def iteracyjny(n, a, x):
    w = a[0]
    for i in range(1, n):
        w = w*x + a[i]
    return w

def rekurencyjny(a, x, i):
    i -= 1
    w = a[i]
    if i == 0:
        return w
    w = rekurencyjny(a, x, i)*x + a[i]
    return w

print(iteracyjny(n, a, X))
print(rekurencyjny(a, X, n))
