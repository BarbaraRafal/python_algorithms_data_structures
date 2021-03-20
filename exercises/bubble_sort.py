# pierwsza wstępna wersja
def sort(data: list) -> list:
    for _ in range(len(data) - 1):
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data


##  introduced right_border

def sort(data: list) -> list:
    right_border = len(data) - 1
    while right_border != 0:
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        right_border -= 1
    return data


if __name__ == "__main__":
    sort([5, 4, 3, 2, 1])
