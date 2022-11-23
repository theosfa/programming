print("Zaszyfrujmy i deszyfrujmy tekst z pliku stosując płot o wysokości 3 wierszy.")

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

wiersz = 3

def codify_string(txt: str) ->str:
    l = ''
    l1 = ''
    for i in range(0, len(txt), wiersz + 1):

        l1 = l1.__add__(list(txt)[i])
    l2 = ''
    for i in range(1, len(txt), wiersz - 1):

        l2 = l2.__add__(list(txt)[i])
    l3 = ''
    for i in range(2, len(txt), wiersz + 1):

        l3 = l3.__add__(list(txt)[i])
    l = l + l1 + l2 + l3
    return l

def codify_list(txt: str) -> list:
    list1 = [[],
             [],
             []]
    for i in range(0, len(txt), wiersz + 1):
        list1[0].append(list(txt)[i])
    for i in range(1, len(txt), wiersz - 1):
        list1[1].append(list(txt)[i])
    for i in range(2, len(txt), wiersz + 1):
        list1[2].append(list(txt)[i])
    return list1


def decodify(list1:list, txt: str) ->list:
    l_res1 = [None] * len(txt)

    num1 = 0
    num2 = 0
    num3 = 0
    for i in range(0, len(txt), 1):
        if i % 4 == 0 or i == 0:
            l_res1[i] = str(list1[0][num1])
            num1 += 1
        elif i % 2 == 0:
            l_res1[i] = str(list1[2][num2])
            num2 += 1
        elif i % 2 != 0:
            l_res1[i] = str(list1[1][num3])
            num3 += 1
    return l_res1


for p in range(0, len(file)):
    print(codify_string(file[p]))

for p in range(0, len(file)):
    for i in codify_list(str(file[p])):
        print('\t'.join(map(str, i)))

for p in range(0, len(file)):
    print(decodify(codify_list(file[p]), file[p]))


print(decodify(codify_list(file[0]), file[0]))

input()
