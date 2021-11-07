def is_anagram(string1, string2) ->bool:
    if len(string1) != len(string2):
        return False

    string1 = string1.lower()
    string2 = string2.lower()

    char_list =[0 for i in range(26)]

    for char in string1:
        idx = ord(char) - 97
        char_list[idx] += 1

    for char in string2:
        idx = ord(char) - 97
        char_list[idx] -= 1

    for count in char_list:
        if count != 0:
            return False
    return True


def is_anagram1(string1, string2):
    if len(string1) != len(string2):
        return False

    char_to_count = {}
    for char in string1:
        if char in char_to_count:
            char_to_count[char] += 1
        else:
            char_to_count[char] = 1

    for char in string2:
        if char in char_to_count:
            char_to_count[char] -= 1
        else:
            return False

    for k, v in char_to_count.items():
        if v != 0:
            return False
    return True


if __name__ == '__main__':
    print(is_anagram1("knee", "keen"))
    print(is_anagram1("earth", "heart"))
    print(is_anagram1("pear", "peer"))
    print(is_anagram1("keen", "kneel"))

    # list of all chars init with 0
    # iterate first string and increase char count in the list
    # iterate second sting and decrease char count
    # iterate the chars list and see if all count is zero

    # char_to_count = {
    #     "a": 0
    # }
    #
    # print("b" in char_to_count)
    # char_to_count["b"] = 2
    # char_to_count["c"] = 3
    # print("b" in char_to_count)
    #
    # print(char_to_count["b"])
    #
    # print(char_to_count.items())
    # for k, v in char_to_count.items():
    #     print(k, v)
    #
    # print(char_to_count.keys())
    # print(char_to_count.values())










