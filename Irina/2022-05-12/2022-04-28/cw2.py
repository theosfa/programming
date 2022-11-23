"""Dana jest tabela zawierająca przykładowe zbiory liczbowe 𝐴 oraz liczby pierwsze 𝑝. W zbiorze 𝐴
zawarte są boki potencjalnego prostokąta.
Dla dowolnego wiersza tabeli należy znaleźć największe pole 𝑆 prostokąta (przy czym nie może on być
kwadratem), które nie jest podzielne przez 𝑝. Jeśli taki prostokąt nie istnieje, to jego pole wynosi zero.
Zbiór liczbowy 𝑨 Liczba pierwsza 𝒑 Pole szukanego prostokąta
7, 5, 11, 33
15, 12, 10, 6, 5, 1
6, 28, 7, 12, 10, 14, 5, 9, 4, 8, 18
4, 34, 16, 8, 6, 22, 14, 12, 2, 7
Na podstawie powyższych informacji napisz program, który działa według przedstawionego opisu dla
pojedynczego wiersza tabeli (wersja łatwiejsza) albo analizuje wszystkie wiersze tabeli (wersja
trudniejsza)"""

list_of_p = [3, 5, 7, 2]

list_of_numbers = [
    [7, 5, 11, 33, 3],
    [15, 12, 10, 6, 5, 1],
    [6, 28, 7, 12, 10, 14, 5, 9, 4, 8, 18],
    [4, 34, 16, 8, 6, 22, 14, 12, 2, 7]
]


# lista = [6, 28, 7, 12, 10, 14, 5, 9, 4, 8, 18]
# print(list_of_numbers[2])
def find_square():
    list_of_sums = []
    for u in range(0, 4):
        suma = 0
        square = []
        for i in range(0, len(list_of_numbers[u])):
            for k in range(0, len(list_of_numbers[u])):
                if list_of_numbers[u][i] == list_of_numbers[u][k]:
                    # print(list_of_numbers[u][i], " ", list_of_numbers[u][k])
                    break
                square.append(list_of_numbers[u][i] * list_of_numbers[u][k])
                # print(square)

                for l in range(0, len(square)):
                    if square[l] % list_of_p[u] != 0:
                        if square[l] > suma:
                            suma = square[l]
        list_of_sums.append(suma)

    return list_of_sums


print("List of numbers: ")
for i in list_of_numbers:
    print('\t'.join(map(str, i)))

print("List of liczb pierwsze: ", list_of_p)
print("Pole szukanego prostokąta", str(find_square()))
input()
