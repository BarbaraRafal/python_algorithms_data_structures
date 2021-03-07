"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the
 value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."""


def reverse(x: int) -> int:
    x_list = []
    minus_list = []
    if x < 0:
        x = abs(x)
        minus_list.append("-")
    for element in str(x):
        if element[-1] == 0:
            continue
        else:
            x_list.append(element)
    x_list.reverse()
    reversed_list = minus_list + x_list
    reversed_int = int("".join(reversed_list))
    if -231 <= reversed_int <= 231 - 1:
        return reversed_int
    else:
        return 0


if __name__ == "__main__":
    print(reverse(-250))

    print(reverse(123))

    print(reverse(256))

