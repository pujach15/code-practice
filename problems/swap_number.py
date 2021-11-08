def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


if __name__ == "__main__":
    a = [0, 2, 4, 6, 8, 1]
    swap(a, 2, 4)
    print(a)
