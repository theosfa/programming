a = 1
b = 1
P = 34
S = 0
for i in range(P//2):
    for j in range(P//2):
        if (i+j)*2 == P:
            if i*j > S:
                S = i*j
                a = i
                b = j
print(a)
print(b)
print(S)
