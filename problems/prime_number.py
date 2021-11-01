import math


def is_prime(num: int) -> bool:
    if num == 0 or num == 1:
        return False

    if num == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def check_prime_in_range(start: int, end: int) -> list:
    arr = []
    for num in range(start, end):
        if is_prime(num):
            arr.append(num)
    return arr


if __name__ == "__main__":
    res = check_prime_in_range(3000, 3024)
    print(res)

    print(is_prime(3023))
