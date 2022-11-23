najlepsza = 0
n = 14
a = [2, 3, -2, 3, -5, -1, 2, -1, 3, -2, 4, -1, 2, -1]
for i in range(n):
    for j in range(i, n):
        suma = 0
        for k in range(i, j+1):
            suma = suma + a[k]
        if(suma > najlepsza):
            najlepsza = suma
print(najlepsza)
