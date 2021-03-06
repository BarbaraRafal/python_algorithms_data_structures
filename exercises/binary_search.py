from typing import List, Optional


def search(items: List[int], target: int) -> Optional[int]:
    left, right = 0, len(items) - 1
    count = 0
    while left <= right:
        count += 1
        middle = left + (right - left) // 2
        if items[middle] == target:
            print(f"Total iterations : {count}")
            return middle
        if items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    print(f"Total iterations: {count}")
    return None


if __name__ == "__main__":
    data = range(1000)

    assert search(data, 1001) is None
    assert search(data, 10) == 10
