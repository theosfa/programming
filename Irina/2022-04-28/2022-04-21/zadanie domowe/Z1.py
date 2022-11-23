tekst1 = "algorytm"
tekst2 = "logarytm"

tekst3 = "body"
tekst4 = "bity"
file = []
dane = open("dane_z1.txt", "r")
for k in dane:
    file.append(k.rstrip())

def anagram(text1: str, text2: str) -> int:
    word_len = 0
    l1 = list(text1)
    l2 = list(text2)
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:

                word_len += 1
                l2.pop(j)
                break

    return word_len


def if_words_anagrams(txt1: str, txt2: str) -> str:
    res_anagrams = "are anagrams"
    res_not_anagrams = "are not anagrams"
    if len(txt1) == len(txt2):
        if anagram(txt1, txt2) == len(txt1):
            return res_anagrams
        else:
            return res_not_anagrams
    else:
        return res_not_anagrams


print(tekst1, tekst2, if_words_anagrams(tekst1, tekst2))
print(tekst3, tekst4, if_words_anagrams(tekst3, tekst4))
print(str(file[0]), str(file[1]), if_words_anagrams(str(file[0]), str(file[1])))

input()
