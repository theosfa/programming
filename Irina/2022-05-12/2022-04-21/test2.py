print("Zaszyfrujmy i deszyfrujmy dla przykładu tekst z pliku stosując płot o wysokości 4 wierszy.")

file = []
dane = open("dane_z2.txt", "r")
for k in dane:
    k = k.rstrip().replace(" ", "")
    k = k.rstrip().replace("'", "")
    k = k.rstrip().replace(".", "")
    k = k.rstrip().replace('"', "")
    k = k.rstrip().replace("...", "")
    k = k.rstrip().replace(",", "")
    file.append(k.rstrip())

print(file)

def codify_string(txt: str) ->str:
    l = ''
    l1 = ''
    for i in range(0, len(txt), 6):
        l1 += list(txt)[i]

    l2 = ''

    for i in range(1, len(txt), 2):
        if i % 3 != 0:
            l2 += list(txt)[i]


    l3 = ''
    for i in range(2, len(txt), 2):
        if i % 2 == 0:
            l2 += list(txt)[i]


    l4 = ''
    for i in range(3, len(txt), 6):
        l4 += list(txt)[i]
    l = l + l1 + l2 + l3 + l4
    return l

def codify_list(txt: str) -> list:
    list1 = [[],
             [],
             [],
             []]
    for i in range(0, len(txt), 6):
        list1[0].append(list(txt)[i])
    for i in range(1, len(txt), 2):
        if i % 3 != 0:
            list1[1].append(list(txt)[i])
    for i in range(2, len(txt), 2):
        if i % 2 == 0 and i % 6 != 0:
            list1[2].append(list(txt)[i])
    for i in range(3, len(txt), 6):
        list1[3].append(list(txt)[i])
    return list1


def decodify(list1:list, txt: str) ->list:
    l_res1 = [None] * len(txt)

    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    for i in range(0, len(txt), 1):
        if i % 6 == 0 or i == 0:
            l_res1[i] = str(list1[0][num1])
            num1 += 1
        elif i % 2 != 0 and i % 3 != 0:
            l_res1[i] = str(list1[1][num2])
            num2 += 1
        elif i % 2 == 0:
            l_res1[i] = str(list1[2][num3])
            num3 += 1
        elif i % 3 == 0:
            l_res1[i] = str(list1[3][num4])
            num4 += 1
    return l_res1
#
# print(decodify(codify_list(text), text))


# print(codify_list(file[0]))


print(codify_string(file[0]))

for p in range(0, len(file)):
    for i in codify_list(str(file[p])):
        print('\t'.join(map(str, i)))

for p in range(0, len(file)):
    print(decodify(codify_list(file[p]), file[p]))

input()
