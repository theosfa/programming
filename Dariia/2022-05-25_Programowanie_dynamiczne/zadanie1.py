def podajDane():
    n = int(input("Podaj n : "))
    waga = int(input("Podaj waga : "))
    W = []
    C = []
    Wartosci = []
    Numery = []
    for i in range(n+1):
        if i > 0:
            W.append(int(input(f"Podaj {i} wartosć: ")))
            C.append(int(input(f"Podaj {i} waga: ")))
        else:
            W.append(0)
            C.append(0)
        Wartosci.append([])
        Numery.append([])
        for j in range(waga+2):
            Wartosci[i].append(0)
            Numery[i].append(0)
    return n, waga, W, C, Wartosci, Numery


n = 0
waga = 0
W = []
C = []
Wartosci = []
Numery = []
n, waga, W, C, Wartosci, Numery = podajDane()
while True:
    print("Wybierz:")
    print("1. Tylko jeden raz")
    print("2. Duże raz")
    print("3. Ponowne zapisanie danych")
    print("4. Wyjście")
    wybor = int(input("Wybór : "))
    if wybor == 1:
        for i in range(1, n+1):
            for j in range(1, waga+2):
                if j > C[i] and Wartosci[i-1][j] < Wartosci[i][j-C[i]] + W[i]:
                    Wartosci[i][j] = W[i] + Wartosci[i-1][j]
                    Numery[i][j] = i
                else:
                    Wartosci[i][j] = Wartosci[i-1][j]
                    Numery[i][j] = Numery[i-1][j]
        for i in range(1,n+1):
            buff = ""
            for j in range(2, waga+2):
                buff += str(Wartosci[i][j]) + " "
            print(buff)
        print("---------------------------------------------")
        for i in range(1,n+1):
            buff = ""
            for j in range(2, waga+2):
                buff += str(Numery[i][j]) + " "
            print(buff)
    elif wybor == 2:
        for i in range(1, n+1):
            for j in range(1, waga+2):
                if j > C[i] and Wartosci[i-1][j] < Wartosci[i][j-C[i]] + W[i]:
                    Wartosci[i][j] = W[i] + Wartosci[i][j-C[i]]
                    Numery[i][j] = i
                else:
                    Wartosci[i][j] = Wartosci[i-1][j]
                    Numery[i][j] = Numery[i-1][j]
        for i in range(1,n+1):
            buff = ""
            for j in range(2, waga+2):
                buff += str(Wartosci[i][j]) + " "
            print(buff)
        print("---------------------------------------------")
        for i in range(1,n+1):
            buff = ""
            for j in range(2, waga+2):
                buff += str(Numery[i][j]) + " "
            print(buff)
    elif wybor == 3:
        n, waga, W, C, Wartosci, Numery = podajDane()
    else:
        break
    for i in range(n+1):
        for j in range(waga+2):
            Wartosci[i][j] = 0
            Numery[i][j] = 0
