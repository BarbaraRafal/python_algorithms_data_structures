"""Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2**x.

Example 1:
Input: n = 1
Output: true
Explanation: 2**0 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 2**4 = 16

Example 3:
Input: n = 3
Output: false

Example 4:
Input: n = 4
Output: true

Example 5:
Input: n = 5
Output: false
"""
from math import log


def is_power_of_two(n: int) -> bool:
    if n in [1, 2]:
        return True
    if n == 0:
        return False
    x = log(n) / log(2)
    if x % 2 == 0:
        return True


if __name__ == "__main__":
    print(is_power_of_two(0))
    print(is_power_of_two(16))
    print(is_power_of_two(3))
    print(is_power_of_two(4))
    print(is_power_of_two(5))
    print(is_power_of_two(2))  # ???
