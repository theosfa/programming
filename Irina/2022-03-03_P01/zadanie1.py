n = int(input("How many : "))
super = []
sum = 0

for i in range(1, n+1):
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        super.append(i)
    sum = 0

print(super)
