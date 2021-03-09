"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in
 the range that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.
"""

from typing import List


def missing_number(nums: List[int]) -> int:
    missing = None
    for element in range(0, len(nums)):
        if element not in nums:
            missing = element
    return missing


if __name__ == "__main__":
    print(missing_number([3, 0, 1]))
    print(missing_number([8, 7, 6, 5, 2, 1, 3, 0]))
