def pyramid(n):
    """
    ---*---
    --***--
    -*****-
    *******
    :param n:
    :return:
    """
    i = 1
    while i <= (n+1)//2:
        for j in range((n-2*i+1)//2):
            print("-", end="")
        for j in range(2*i-1):
            print("*", end="")
        for j in range((n-2*i+1)//2):
            print("-", end="")
        i += 1
        print()


if __name__ == '__main__':
    pyramid(7)
    # pyramid(11)