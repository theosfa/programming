n = int(input("Wpisz numer: "))

for i in range (1, n):
    sum_i = 0
    for i_ in range(1, i):
        if i % i_ == 0:
            sum_i += i_

    for j in range(i+1, n):
        sum_j = 0
        for j_ in range(1, i):
            if j % j_ == 0:
                sum_j += j_
        if sum_j == i and sum_i == j:
            print(i, j)
