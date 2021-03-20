"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of
the two sorted arrays.

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
"""


def merge(left: list, right: list) -> list:
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    size1, size2 = len(left), len(right)
    i, j = 0, 0
    while i < size1 and j < size2:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def median(left: list, right: list) -> float:
    data = merge(left, right)
    size = len(data)
    if size == 1:
        return data[0]
    if size % 2 == 1:
        return data[size // 2]
    l, r = (size - 1) // 2, (size + 1) // 2
    return (data[l] + data[r]) / 2.0


if __name__ == "__main__":
    a = [1, 2, 5]
    b = [3, 4]
    assert median(a, b) == 3
