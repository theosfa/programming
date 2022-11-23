print("Zaszyfrujmy i deszyfrujmy wyraz KRYPTOANALIZA stosując płot o wysokości 3 wierszy.")
text = "KRYPTOANALIZA"
text = text.replace(" ", "")


wiersz = 3

def codify_string(txt: str) ->str:
    l = ''
    l1 = ''
    for i in range(0, len(text), wiersz + 1):

        l1 += list(text)[i]
    l2 = ''
    for i in range(1, len(text), wiersz - 1):

        l2 += list(text)[i]
    l3 = ''
    for i in range(2, len(text), wiersz + 1):

        l3 += list(text)[i]
    l = l + l1 + l2 + l3
    return l

def codify_list(txt: str) -> list:
    list1 = [[],
             [],
             []]
    for i in range(0, len(text), wiersz + 1):
        list1[0].append(list(text)[i])


    for i in range(1, len(text), wiersz - 1):
        list1[1].append(list(text)[i])


    for i in range(2, len(text), wiersz + 1):
        list1[2].append(list(text)[i])


    return list1

print(codify_string(text))

for i in codify_list(text):
    print('\t'.join(map(str, i)))

def decodify(list1:list) ->list:
    l_res1 = [None] * len(text)

    num1 = 0
    num2 = 0
    num3 = 0
    for i in range(0, len(text), 1):
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

print(decodify(codify_list(text)))

input()
