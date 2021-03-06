# liczymy silnię
# 5! = 5*4*6*2*1 = 120
# 1! = 1
# 0! = 1
# w iteracji
def factorial(n: int) -> int:
    if n in [0, 1]:
        return 1
    p = 1
    for i in range(2, n + 1):
        p *= i
    return p


# w rekurencji( rekursji)
def factorial_2(n: int) -> int:
    if n in [0, 1]:
        return 1
    return n * factorial_2(n - 1)


# factorial_2(3) = 6
# 3* factorial_2(2) | 3*2*1
# 2 * factorial2(1) =1 | 2*1
if __name__ == "__main__":
    print(factorial_2(3))
