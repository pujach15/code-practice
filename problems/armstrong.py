# an armstrong number is a number that follows
# d = length(num)
# sum of all digits raised to the power d equals to that number
# 153 = 1^3 + 5^3 + 3^3, hence an armstrong number

def is_armstrong(num: int) -> bool:
    d = 0
    n = s = num
    arm = 0
    while n > 0:
        n = int(n / 10)
        d += 1

    while num > 0:
        a = num % 10
        arm += a ** d
        num = int(num / 10)

    return s == arm


def check_armstrong_in_range(start: int, end: int) -> list:
    arr = []
    for num in range(start, end):
        if is_armstrong(num):
            arr.append(num)

    return arr


if __name__ == "__main__":
    res = check_armstrong_in_range(10, 10000)
    print(res)
