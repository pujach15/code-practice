
def fibonacci(size):
    num1 = 0
    num2 = 1
    arr = [num1, num2]
    for i in range(2, size):
        c = num1 + num2
        arr.append(c)
        num1 = num2
        num2 = c

    return arr


if __name__ == "__main__":
    res = fibonacci(10)
    print(res)

