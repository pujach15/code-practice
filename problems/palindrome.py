def is_palindrome(n) -> bool:
    num = n
    rem = 0
    reverse = 0
    if isinstance(n, int):

        while n>0:
            rem = n%10
            reverse = reverse * 10 + rem
            n = int(n / 10)

        print(num, reverse)

        if num == reverse:
            return True
        else:
            return False

    if isinstance(n, str):
        i, j = 0, len(num) - 1
        while i < j:
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1

        return True

       # reverse = n[::-1]
       # if num == reverse:
       #     return True
       # else:
       #     return False


if __name__ == '__main__':
    print(is_palindrome(5421245))
    print(is_palindrome("madam"))
    print(is_palindrome("mada"))

