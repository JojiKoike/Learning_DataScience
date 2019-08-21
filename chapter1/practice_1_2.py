import os


def summation(i: int) -> int:
    res = 0
    for i in range(1, i + 1):
        res += i
    return res


if __name__ == '__main__':
    print(summation(50))
