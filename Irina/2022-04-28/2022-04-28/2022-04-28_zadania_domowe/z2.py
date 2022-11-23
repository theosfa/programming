nterms = int(input("How long the field is? "))

table = [int(input(f"T[{i}]=")) for i in range(nterms + 1)]

print(table)

def fibonacci():
    fib = []

    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        fib.append(n1)
        fib.append(n2)
        while count < nterms:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
            fib.append(nth)
    return fib



fibo = fibonacci()


def road(way: list) -> int:
    count = 0
    current_u = 0

    for u in range(0, len(way)):
        if way[u] == 0:
            dif = u - current_u
            for j in range(0, len(fibo) - 1):

                if dif == fibo[j] and dif != 0:
                    current_u = u
                    count += 1
                    break
                else:

                    if j == len(fibo) - 2:
                        break
                    else:
                        continue

    return count

wyniki = open("wyniki_c2.txt", "w")
wyniki.write("Length of field is ")
wyniki.write(str(nterms))
wyniki.write('\n')
wyniki.write(str(table))
wyniki.write('\n')
wyniki.write("A rabbit has to jump ")
wyniki.write(str(road(table)))
wyniki.write("times to cross the field")
