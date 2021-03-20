"""Proszę napisać funkcję validate(sequence: str) -> bool, która sprawdza czy przekazana
sekwencja nawiasów jest poprawna.
Przykład:
validate("()()()") => True
validate("()(") => False # dlatego że jeden nawias nie jest zamknięty"""


def validate(sequence: str) -> bool:
    stack = []
    for character in sequence:
        if character not in ["(",")"]
            continue
        if character == "(":
            stack.append(character)
        else:
            if len(stack) == 0:
                return  False
            else:
                stack.pop()
    return len(stack) == 0



if __name__ == "__main__":
    assert validate("(())") == True
    assert validate("(()") == False
