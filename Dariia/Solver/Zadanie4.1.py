A = 2
B = 3
answer = 0
primary_ans = 0
secondary_ans = 0
min_ans = 1000
how_many = int(input("How many? "))
buff_litr = how_many
how_A = 0
how_B = 0
for i in reversed(range(how_many+1)):
    answer = i
    primary_ans = i
    buff_litr -= answer*2
    secondary_ans  = 0
    while buff_litr > 0:
        buff_litr -= 3
        answer += 1
        secondary_ans += 1
    if answer < min_ans :
        min_ans = answer
        how_A = primary_ans
        how_B = secondary_ans
    buff_litr = how_many
print(min_ans)
print(how_A)
print(how_B)
