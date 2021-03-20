"""Given an array nums of n integers, are there elements a, b, c in nums such
 that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:66666++++++++++++++++++++++++++++++++++++++++++
Input: nums = [0]
Output: []
"""
from typing import List, Tuple


def three_sum(nums: List[int], target: int = 0) -> Tuple[int, int, int]:
    triplets = []
    i = 0
    end = len(nums)
    for i in range(len(nums)-1):
        while i <= end - 3:
            value = nums[i] + nums[i + 1] + nums[i + 2]
            if value == target:
                triplets.append([nums[i], nums[i + 1], nums[i + 2]])
            i += 1
    return triplets


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))
