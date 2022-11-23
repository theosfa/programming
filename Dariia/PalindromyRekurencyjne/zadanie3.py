
def spruce(n, i=1):
    if i <= n * 2:
        print(("*" * i).center(n * 2, " "))
        spruce(n, i + 2)
    else:
        print(" "*(n-1) + "#")
n = 6
spruce(n)
