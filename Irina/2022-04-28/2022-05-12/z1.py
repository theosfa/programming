liczby_wynik = open("liczby.txt", "r")


def prime_number(num: int) -> bool:
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False


def semiprime_number(num: int) -> int:
    result_count = 0
    mult = 1
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
            if prime_number(i) and i != 1:
                result_count += 1
                mult = mult * i
                print(num, i)
    if result_count == 2 and mult == num:
        result = num
    else:
        result = 0
    return result


print(semiprime_number(937))
wyniki = open("wyniki_c1.txt", "w")
for k in liczby_wynik:
    if semiprime_number(int(k.rstrip())) != 0:
        wyniki.write(k)

input()
