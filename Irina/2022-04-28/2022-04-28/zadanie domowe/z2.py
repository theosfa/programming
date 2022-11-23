rabbit_way = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0]



nterms = int(input("How many terms? "))


def fibonacci():
    fib = []

    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        fib.append(n1)
        fib.append(n2)
        while count < nterms:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
            fib.append(nth)
    return fib


print(fibonacci())
fibo = fibonacci()


def road():
    count = 0
    for u in range(0, len(rabbit_way)):
        if rabbit_way[u] == 0:
            for j in range(0, nterms-1):
                if u == fibo[j]:
                    count += 1
                else:
                    continue
    return count


print(road())
