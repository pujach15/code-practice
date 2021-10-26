

def add(a, b):
    return a+b


a = 3
b = 5


# create a function named table, parameter: int
def table(a):
    for i in range(1, 11):
        d = f"{a} * {i} = {a * i}"
        print(d)


# table(294)


# create a function that returns a list of table values(from 1 to 10) given an integer
# return [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
def table_values(num):
    a = []
    for i in range(1, 11):
        a.append(num * i)

    return a


result = table_values(12)
print(result)






