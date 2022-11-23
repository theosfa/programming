list_of_p = [3, 5, 7, 2]

list_of_numbers = [
    [7, 5, 11, 33, 3],
    [15, 12, 10, 6, 5, 1],
    [6, 28, 7, 12, 10, 14, 5, 9, 4, 8, 18],
    [4, 34, 16, 8, 6, 22, 14, 12, 2, 7]
]


def find_square():
    list_of_sums = []
    for u in range(0, 4):
        suma = 0
        square = []
        for i in range(0, len(list_of_numbers[u])):
            for k in range(0, len(list_of_numbers[u])):
                if list_of_numbers[u][i] == list_of_numbers[u][k]:
                    break
                square.append(list_of_numbers[u][i] * list_of_numbers[u][k])

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
