def check_occurrenc(string, char):

    count = 0
    for i in range(len(string)):
        if string[i] == char:
            count = count + 1

    return count


if __name__ == '__main__':
    print(check_occurrenc("pujaa", "a"))
