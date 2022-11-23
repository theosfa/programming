s = "привіт як твоі справи."
vouls = "аеёіуиюя"

vouls_sort = {
    "а" : 1,
    "е" : 2,
    "ё" : 3,
    "і" : 4,
    "у" : 5,
    "и" : 6,
    "ю" : 7,
    "я" : 8,
}

list_s = s.replace(".", "").split(" ")
list_buff = []
for i in list_s:
    buff = ""
    for j in range(len(i)):
        if i[j] in vouls:
            buff += i[j]
    list_buff.append(list(buff))
for i in list_buff:
    for j in range(len(i)):
        for k in range(len(i)-1):
            if vouls_sort[i[k]] > vouls_sort[i[k+1]]:
                buff = i[k]
                i[k] = i[k+1]
                i[k+1] = buff

list_final = []
for i in list_buff:
    buff = ""
    for j in range(len(i)):
        buff += i[j]
    list_final.append(buff)
for i in list_final:
    print(i)
