# Python3 program to illustrate
# Rail Fence Cipher Encryption
# and Decryption

# function to encrypt a message
def encryptRailFence(text, key):

    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    # to find the direction
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):

        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1

        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return ("".join(result))


def decryptRailFence(cipher, key):

    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    # to find the direction
    dir_down = None
    row, col = 0, 0

    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        rail[row][col] = '*'
        col += 1

        # find the next row
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1

    # now we can construct the
    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
                    (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):

        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return ("".join(result))


# Driver code
if __name__ == "__main__":
    print(encryptRailFence("attack at once", 2))
    print(encryptRailFence("GeeksforGeeks ", 3))
    print(encryptRailFence("defend the east wall", 3))

    # Now decryption of the
    # same cipher-text
    print(decryptRailFence("GsGsekfrek eoe", 3))
    print(decryptRailFence("atc toctaka ne", 2))
    print(decryptRailFence("dnhaweedtees alf tl", 3))

print(encryptRailFence("KRYPTOANALIZADANYCH", 4))
print(decryptRailFence(str(encryptRailFence("KRYPTOANALIZADANYCH", 4)), 4))


# file = []
# dane = open("dane_z2.txt", "r")
# for k in dane:
#     k = k.rstrip().replace(" ", "")
#     k = k.rstrip().replace("'", "")
#     k = k.rstrip().replace(".", "")
#     k = k.rstrip().replace('"', "")
#     k = k.rstrip().replace("...", "")
#     k = k.rstrip().replace(",", "")
#     file.append(k.rstrip())
#
# print(file)
#
# w = 5
# def codify_string(txt: str) ->str:
#     l = ''
#     current_l = ''
#     y = 0
#     res_a = w - 2
#     print(res_a)
#     for u in range(0, w, 1):
#         if y == 0:
#             for i in range(u, len(txt), 1):
#                 if i == y or (i % (w+res_a) == 0 and i % 2 == 0):
#                     current_l += list(txt)[i]
#             l += current_l
#             current_l = ''
#             y += 1
#             if i == len(txt):
#                 break
#         elif y == 1:
#             for i in range(y, len(txt), 2):
#                 if i == y or (i % 2 != 0 and i % (w - 1) != 0):
#                     current_l += list(txt)[i]
#             l += current_l
#             current_l = ''
#             y += 1
#             if i ==len(txt):
#                 break
#         elif y == 2:
#             for i in range(y, len(txt), 2):
#                 if i == y or (i % 2 == 0 and i % (w + res_a) != 0):
#                     current_l += list(txt)[i]
#             l += current_l
#             current_l = ''
#             y += 1
#             if i ==len(txt):
#                 break
#
#         elif y == w-1:
#             for i in range(y, len(txt), 2):
#                 if i == y or (i % 2 != 0 and i % (w - 1) == 0):
#                     current_l += list(txt)[i]
#             l += current_l
#             current_l = ''
#             y += 1
#             if i ==len(txt):
#                 break
#     return l
#
#
# print(codify_string("KRYPTOANALIZA"))
# # def codify_list(txt: str) -> list:
# #     list1 = [[],
# #              [],
# #              [],
# #              []]
# #     for i in range(0, len(txt), 6):
# #         list1[0].append(list(txt)[i])
# #     for i in range(1, len(txt), 2):
# #         if i % 3 != 0:
# #             list1[1].append(list(txt)[i])
# #     for i in range(2, len(txt), 2):
# #         if i % 2 == 0 and i % 6 != 0:
# #             list1[2].append(list(txt)[i])
# #     for i in range(3, len(txt), 6):
# #         list1[3].append(list(txt)[i])
# #     return list1
#
#
# # def decodify(list1:list, txt: str) ->list:
# #     l_res1 = [None] * len(txt)
# #
# #     num1 = 0
# #     num2 = 0
# #     num3 = 0
# #     num4 = 0
# #     for i in range(0, len(txt), 1):
# #         if i % 6 == 0 or i == 0:
# #             l_res1[i] = str(list1[0][num1])
# #             num1 += 1
# #         elif i % 2 != 0 and i % 3 != 0:
# #             l_res1[i] = str(list1[1][num2])
# #             num2 += 1
# #         elif i % 2 == 0:
# #             l_res1[i] = str(list1[2][num3])
# #             num3 += 1
# #         elif i % 3 == 0:
# #             l_res1[i] = str(list1[3][num4])
# #             num4 += 1
# #     return l_res1
# #
# # print(decodify(codify_list(text), text))
#
#
# # print(codify_list(file[0]))
#
#
#
#
# # for p in range(0, len(file)):
# #     for i in codify_list(str(file[p])):
# #         print('\t'.join(map(str, i)))
# #
# # for p in range(0, len(file)):
# #     print(decodify(codify_list(file[p]), file[p]))
