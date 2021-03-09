"""Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

from math import pow


def my_pow(x: float, n: int) -> float:
    if n == 0:
        return 1
    elif n > 0:
        result = x ** n
    else:
        result = 1 / x ** abs(n)
    return result


if __name__ == "__main__":
    print(my_pow(5, -2))
    print(my_pow(5.5, -2))
    print(my_pow(10, -3))
    print(my_pow(2, 2))

    ##  below imported pow() function from math module just to check results

    print(pow(5, -2))
    print(pow(5.5, -2))
    print(pow(10, -3))
    print(pow(2, 2))
