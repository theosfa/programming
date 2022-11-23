
price_min = 0
price_max = 0
numbers = int(input("Write down numbers of array : ")) #3
array = []
array_min = []
array_max = []
for index in range(numbers):
    array.append(int(input()))

for j in range(numbers):
    for index in range(numbers - 1):
        if array[index] > array[index + 1]:
            buff = array[index]
            array[index] = array[index + 1]
            array[index + 1] = buff
for index in range(numbers):
    array_min.append(array[index])

for j in range(numbers):
    for index in range(numbers - 1):
        if array[index] < array[index + 1]:
            buff = array[index]
            array[index] = array[index + 1]
            array[index + 1] = buff
for index in range(numbers):
    array_max.append(array[index])

print(array)
pointer = 0
number_of_search = 0
number_of_sums = 0
for p in range(numbers - 1):
    price_min += array_min[pointer] + array_min[pointer+1]
    array_min[pointer+1] += array_min[pointer]
    array_min[pointer] = 0
    number_of_sums += 1
    number_of_search += 1
    for index in range(numbers - 1):
        if array_min[index] > array_min[index + 1]:
            buff = array_min[index]
            array_min[index] = array_min[index + 1]
            array_min[index + 1] = buff
            number_of_search += 1
    pointer += 1
    print(array_min)
print(f"{price_min}, {number_of_sums}, {number_of_search}")

number_of_search = 0
number_of_sums = 0
for p in range(numbers - 1):
    price_max += array_max[0] + array_max[1]
    array_max[1] += array_max[0]
    array_max[0] = 0
    number_of_sums += 1
    number_of_search += 1
    for index in range(numbers - 1):
        if array_max[index] < array_max[index + 1]:
            buff = array_max[index]
            array_max[index] = array_max[index + 1]
            array_max[index + 1] = buff
            number_of_search += 1
    print(array_max)
print(f"{price_max}, {number_of_sums}, {number_of_search}")
print(f"Min price = {price_min}, max price = {price_max}")
