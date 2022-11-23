A = 3
B = 5
C = 7
answer = 0
primary_ans = 0
secondary_ans = 0
min_ans = 1000
how_many = int(input("How many? "))
buff_litr = how_many
how_A = 0
how_B = 0
if how_many == 1:
    min_ans = 3
    how_A  = 3
    how_B  = 0
elif how_many == 2:
    min_ans = 2
    how_A = 0
    how_B = 2
else:
    for i in reversed(range(how_many+1)):
        answer = i
        primary_ans = i
        buff_litr -= answer*A
        secondary_ans  = 0
        while buff_litr > 0:
            if buff_litr == 1:
                buff_litr -= 1
                answer += 3
                primary_ans  += 3
            elif buff_litr == 2:
                buff_litr -= 2
                answer += 2
                secondary_ans  += 2
            if buff_litr >= B:
                buff_litr -= B
                answer += 1
                secondary_ans += 1
            else:
                break
        if answer < min_ans and buff_litr == 0:
            min_ans = answer
            how_A = primary_ans
            how_B = secondary_ans
        buff_litr = how_many
print(min_ans)
print(how_A)
print(how_B)
