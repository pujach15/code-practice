def factorial(n):
    val = 1
    for i in range(n,1,-1):
        val = val * i

    return val


if __name__ == '__main__':
    print(factorial(5))
    print(factorial(6))
