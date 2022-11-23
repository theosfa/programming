n = int(input("How many : "))
super = []
friendly = []
sum = 0

for i in range(1, n+1):
    for j in range(1, i):
        if i % j == 0:
            sum += j
    super.append((i, sum))
    sum = 0
for i in range(len(super)):
    for j in range(i+1, len(super)):
        if super[i][0] == super[j][1] and super[i][1] == super[j][0]:
            friendly.append((super[i][0], super[j][0]))

print(super)
print(friendly)
