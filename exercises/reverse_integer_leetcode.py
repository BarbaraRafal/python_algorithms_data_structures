"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the
 value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."""


def reverse(x: int) -> int:
    x_list = []
    for element in str(abs(x)):
        if element[-1] == 0:
            continue
        else:
            x_list.append(element)
    x_list.reverse()
    reversed_int = int("".join(x_list))
    if x < 0:
        reversed_int *= -1
    return reversed_int


if __name__ == "__main__":
    print(reverse(-25000))

    print(reverse(123))

    print(reverse(256))
