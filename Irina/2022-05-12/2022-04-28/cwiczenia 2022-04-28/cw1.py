"""Ćwiczenie 1.
Liczbę naturalną 𝑛 nazywamy osiągalną, jeśli istnieje takie 𝑘, że 𝑛 = 𝑘 + 𝑠(𝑘), gdzie 𝑘 jest liczbą
naturalną, a 𝑠(𝑘) jest sumą cyfr liczby 𝑘 w zapisie dziesiętnym.
Przykładowo, liczba 𝑛 = 28 jest osiągalna, ponieważ istnieje liczba 𝑘 = 23, dla której 𝑠(𝑘) = 5, a w
związku z tym 𝑘 + 𝑠(𝑘) = 28 = 𝑛. Podobnie liczba 𝑛 = 505 jest osiągalna, ponieważ 𝑠(𝑘) = 14 dla
𝑘 = 491. Natomiast liczba 𝑛 = 31 nie jest osiągalna, bo nie istnieje liczba 𝑘 spełniająca podane
założenia.
Na podstawie powyższych informacji napisz program, który sprawdza, czy podana przez użytkownika
czterocyfrowa liczba naturalna jest osiągalna (wersja łatwiejsza) albo (wersja trudniejsza) generuje
wszystkie liczby osiągalne z zakresu [1000, 9999]."""

n = int(input("Write a number [1000,9999]: "))


def reachable_number(num: int) -> int:
    if int(num / 1000) != 0:
        for k in range(1, num):
            k1 = int(k / 1000)
            k2 = int(k % 1000 / 100)
            k3 = k % 100 / 10
            k4 = k % 10
            if k + (int(k1) + int(k2) + int(k3) + k4) == num:
                # print(k)
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
