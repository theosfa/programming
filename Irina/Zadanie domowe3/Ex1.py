n = int(input("Podaj numer: "))
suma = 0

#for n in range (1,p,1):

for i in range(1, n, 1):

    if n % i == 0:
        suma = suma+i
        print(suma)


if suma == n:
    print(suma)
else:
    print("nie doskonala liczba")
#print(current_number)





n = int(input("Podaj numer: "))

for i in range(1, n + 1):
    sum_ = 0
    for j in range(1, i):
        if i % j == 0:
            sum_ += j
    if sum_ == i:
        print('!!!!!!!!!!!', i)



#Ex2
