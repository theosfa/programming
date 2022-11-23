dane_matrix = []
dane = open("dane.txt", "r")
wyniki = open("dane_wyniki.txt", "w")
for k in dane:
    dane_row_str = k.split()
    dane_row_int = list(map(int, dane_row_str))
    dane_matrix.append(dane_row_int)

minimum = dane_matrix[0][0]
maximum = dane_matrix[0][0]
for row in dane_matrix:
    for element in row:
        if element < minimum:
            minimum = element
        if element > maximum:
            maximum = element


wyniki.write("Minimum pixel is:")
wyniki.write(str(minimum))
wyniki.write("\n")
wyniki.write("Maximum pixel is:")
wyniki.write(str(maximum))
print(minimum)
print(maximum)

wyniki.write("\n")



dane_matrix = []
dane = open("dane.txt", "r")
for k in dane:
    dane_row_str = k.split()
    dane_row_int = list(map(int, dane_row_str))
    dane_matrix.append(dane_row_int)


def is_row_symmetric(row: list[int]) -> bool:
    return row == row[::-1]


not_symmetric_count = 0
for row in dane_matrix:
    if not is_row_symmetric(row):
        not_symmetric_count += 1


for row in dane_matrix:
    if is_row_symmetric(row):
        r = ' '.join(str(x) for x in row)
        wyniki.write(r)
        wyniki.write('\n')
print(not_symmetric_count)


def is_contrast(a: int, b: int) -> bool:
    return abs(a - b) > 128


def has_contrast_neighbour(matrix: list[list[int]], i: int, j: int) -> bool:
    result = False
    if 0 <= i-1 <= 199:
        result |= is_contrast(matrix[i][j], matrix[i-1][j])
    if 0 <= i+1 <= 199:
        result |= is_contrast(matrix[i][j], matrix[i+1][j])

    if 0 <= j-1 <= 319:
        result |= is_contrast(matrix[i][j], matrix[i][j-1])
    if 0 <= j+1 <= 319:
        result |= is_contrast(matrix[i][j], matrix[i][j+1])

    return result


contrast_count = 0
for i in range(0, 200):
    for j in range(0, 320):
        if has_contrast_neighbour(dane_matrix, i, j):
            contrast_count += 1


wyniki.write("The number of contrast pixels is: ")
wyniki.write(str(contrast_count))
wyniki.write("\n")
print(contrast_count)

input()
