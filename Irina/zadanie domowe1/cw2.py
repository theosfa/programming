dane = open("dane_c2.txt", "r")
wyniki = open("wyniki_c2.txt", "w")
numbers_0_9 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


num = ""
num1 = ""
num2 = ""
nums = ""
for k in dane:
    print(nums)
    l_num = list(k.rstrip())
    print(l_num)

    for j in range(len(k.rstrip())):
        for i in range(10):
            if " " in l_num[j]:
                num1 = num
            if numbers_0_9[i] in l_num[j]:
                if num1 != "":
                    num2 = num2 + l_num[j]
                print(l_num[j])
                num = num + l_num[j]
    nums = int(num1) * int(num2)
    if 250 < nums < 10000:
        wyniki.write(str(nums) + "\n")
    num = ""
    num1 = ""
    num2 = ""
    nums = ""


dane.close()
wyniki.close()

input()

