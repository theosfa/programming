import math

decNum = int(input())
binNum = ''
while decNum > 0:
    binNum = str(decNum % 2) + binNum
    decNum = decNum // 2

print(binNum2)
print(binNum)
