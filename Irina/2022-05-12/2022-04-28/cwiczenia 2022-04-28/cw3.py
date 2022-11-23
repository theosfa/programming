'''Ćwiczenie 3.
Dane są dwie tablice 𝐴 i 𝐵. Każda z nich zawiera 1000 losowo wybranych liczb naturalnych z przedziału
od 1 do 2000. Należy sprawdzić, czy sumy elementów obu tablic są takie same. Jeśli nie, to należy
sprawdzić, czy jest możliwa operacja wielokrotnej zamiany elementów między tablicami w taki sposób,
by po zamianie suma elementów tablicy 𝐴 była równa sumie elementów tablicy 𝐵. Jeśli taka operacja
jest możliwa, należy wskazać te elementy tablic, które należy zamienić między sobą, by doprowadzić
do stanu równowagi.
'''

import random
from itertools import combinations
from typing import Optional


def calculate_balance(list_1: list[int], list_2: list[int]) -> Optional[tuple[tuple[int], tuple[int]]]:
    """
    Try to balance sum of two lists of equal len
    If already balances - return None
    If possible - return first the pair of two shortest sublist, that could be exchanged
    If not possible - raise exception
    """
    assert len(list_1) == len(list_2)
    list_1 = sorted(list_1)
    list_2 = sorted(list_2)

    list_len = len(list_1)

    sum_1 = sum(list_1)
    sum_2 = sum(list_2)
    delta = sum_1 - sum_2
    half_delta = delta // 2

    if delta == 0:
        return
    elif delta % 2 != 0:
        raise ValueError(f"Definitely impossible: delta {delta} is odd")
    else:
        for subset_len in range(list_len):
            print(f"Calculating for subsets of len {subset_len}/{list_len}")
            for sub_A in combinations(list_1, subset_len):
                for sub_B in combinations(list_2, subset_len):
                    if sum_1 - sum_2 == half_delta:
                        return sub_A, sub_B
    raise ValueError("Impossible")


lista_A = []
lista_B = []

LIST_LEN = 1000
MAX_NUM = 2000

for i in range(LIST_LEN):
    rand_A = random.randint(1, MAX_NUM)
    lista_A.append(rand_A)
    rand_B = random.randint(1, MAX_NUM)
    lista_B.append(rand_B)

print(lista_A)
print(lista_B)

print(sum(lista_A), sum(lista_B))
print(calculate_balance(lista_A, lista_B))

input()
