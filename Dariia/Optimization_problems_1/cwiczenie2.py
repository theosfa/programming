n = int(input("Number of elements "))
weight = int(input("Weight of backpack "))
W = []
C = []
K = []
answer = 0
for i in range(n):
    W.append(int(input(f"Price of {i+1} element ")))
    C.append(int(input(f"Weight of {i+1} element ")))

for j in range(n):
    for index in range(n-1):
        if W[index]/C[index] < W[index+1]/C[index+1]:
            buff = W[index]
            W[index] = W[index + 1]
            W[index + 1] = buff
            buff = C[index]
            C[index] = C[index + 1]
            C[index + 1] = buff

for i in range(n):
    K.append(weight//C[i])
    weight -= K[i]*C[i]
    answer += W[i]*K[i]

print(answer)
print(K)
