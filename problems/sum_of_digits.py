def sum_of_digits(n):
    val = 0
    if isinstance(n, int):
        while n > 0:
            a = n % 10
            n = int(n / 10)
            val += a

    if isinstance(n, str):

        for char in n:
            num = int(char)
            val += num

    return val


# def sum_(num):
#     if isinstance(num, str):
#         return sum([int(char) for char in num])


if __name__ == '__main__':
    print(sum_of_digits(121))
    print(sum_of_digits(1323421234))
    print(sum_of_digits("12312312"))
    # print(sum_("12312312"))
