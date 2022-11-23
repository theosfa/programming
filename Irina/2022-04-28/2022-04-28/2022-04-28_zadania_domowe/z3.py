from typing import Optional

k = 6
numbers = [5, 3, 5, 5, 5, 2]


def find_leader(nums: list[int]) -> Optional[int]:
    counts = {nums.count(x): x for x in set(nums)}
    if max(counts.keys()) > len(nums) // 2:
        return counts[max(counts.keys())]


def calculate_ways(nums: list[int]) -> int:
    result = 0
    for i in range(1, len(nums)):
        if find_leader(nums[:i]) == find_leader(nums[i:]):
            result += 1
    return result


print(calculate_ways(numbers))
