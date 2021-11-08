def max_number(arr):
    greatest = arr[0]
    for i in range(len(arr)):
        if arr[i]>greatest:
            greatest = arr[i]
    return greatest




if __name__ == '__main__':
    print(max_number([2, 3, 5, 1, 8, 0, 21, 34]))
    print(max_number([5, 7, 2, 8, 2, 0]))
