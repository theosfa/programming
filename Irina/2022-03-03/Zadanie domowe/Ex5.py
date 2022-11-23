n = int(input("Input n "))
m = int(input("Input m "))
array = []



start_x = int(input("Start x = "))-1
start_y = int(input("Start y = "))-1
end_x = int(input("End x = "))-1
end_y = int(input("End y = "))-1
for j in range(m):
    row = input().split(" ")
    for i in range(len(row)):
        row[i] = int(row[i])
    array.append(row)
pointer = 2
if (array[start_y-1][start_x] == 0 and array[start_y+1][start_x] == 0 and array[start_y][start_x-1] == 0 and array[start_y][start_x+1] == 0) or (array[end_y-1][end_x] == 0 and array[end_y+1][end_x] == 0 and array[end_y][end_x-1] == 0 and array[end_y][end_x+1] == 0) :
    print("There is no escape")
else:
    if start_y-1 >= 0 and array[start_y-1][start_x] == 1 :
        array[start_y-1][start_x] = 2
    if start_y+1 < m and array[start_y+1][start_x] == 1 :
        array[start_y+1][start_x] = 2
    if start_x-1 >= 0 and array[start_y][start_x-1] == 1 :
        array[start_y][start_x-1] = 2
    if start_x+1 < n and array[start_y][start_x+1] == 1 :
        array[start_y][start_x+1] = 2
    array[start_y][start_x] = "s"

    for k in range(m*n):
        print(f"Number is {k}")
        for j in range(m):
            for i in range(n):
                print(array[j][i], end = " ")
            print()
        print()
        for j in range(m):
            for i in range(n):
                if array[j][i] == pointer:
                    if j+1 < m and array[j+1][i] == 1:
                        array[j+1][i] = pointer+1
                    if j-1 >= 0 and array[j-1][i] == 1:
                        array[j-1][i] = pointer+1
                    if i-1 >= 0 and array[j][i-1] == 1:
                        array[j][i-1] = pointer+1
                    if i+1 < n and array[j][i+1] == 1:
                        array[j][i+1] = pointer+1
        pointer += 1

        if array[end_y][end_x] > 1:
            print(f"There is escape for {array[end_y][end_x]-1} moves")
            break
    print("Final table")
    for j in range(m):
        for i in range(n):
            print(array[j][i], end = " ")
        print()
