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


if __name__ == '__main__':
    print(is_anagram("knee", "keen"))
    print(is_anagram("earth", "heart"))
    print(is_anagram("pear", "peer"))
    print(is_anagram("keen", "kneel"))

    # list of all chars init with 0
    # iterate first string and increase char count in the list
    # iterate second sting and decrease char count
    # iterate the chars list and see if all count is zero
