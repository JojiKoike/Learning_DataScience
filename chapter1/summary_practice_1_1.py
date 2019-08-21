from typing import List


def calc_prime_num(n: int) -> List[int]:
    n_list: List[int] = range(2, n + 1)


if __name__ == "__main__":
    for i in calc_prime_num(10):
        print(i)
