import random
from itertools import combinations
from typing import Optional


def calculate_balance(list_1: list[int], list_2: list[int]) -> Optional[tuple[tuple[int], tuple[int]]]:

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
