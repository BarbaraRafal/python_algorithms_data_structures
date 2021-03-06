"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

from typing import List

nums = [2, 7, 11, 15]
target = 9


## Jadwigi rozwiązanie
def two_sum(nums: List[int], target: int) -> List[int]:
    for idx1, num1 in enumerate(nums):
        for idx2, num2 in enumerate(nums):
            if idx1 >= idx2:
                continue
            if num1 + num2 == target:
                return [idx1, idx2]


## rozwiązanie trenera
def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    i, j = 0, len(nums) - 1
    data = sorted(nums)
    while i < j:
        value = data[i] + data[j]
        if value > target:
            j -= 1
        if value < target:
            i += 1
        if value == target:
            break
    idx1 = nums.index(data[i])
    if data[i] == data[j]:
        idx2 = nums.index(data[j], idx1 + 1)
    else:
        idx2 = nums.index(data[j])
    return idx1, idx2


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
