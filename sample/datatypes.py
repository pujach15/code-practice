a = 5
b = 2.089
c = "puja"
d = [1,2 ]

# print(type(c))
# print(type(d))
# print(isinstance(c, str))
# print(isinstance(c, float))
# print(isinstance(d, list))


class Student:
    pass


class Teacher:
    pass


std = Student()
print(type(std))
print(isinstance(std, Student))
print(isinstance(std, Teacher))

# list
data = list()
data = []
data.append(1)
data.append(5)
print(data)

# set
data = set()
# data = {1, 2, 4}
data.add(5)
data.add(6)
data.add(5)
print(data)
print(type(data))


# difference between list and set
# 1. list is ordered , set is not ordered
# 2. retrieval time is O(n), retrieval time is O(1)

data = {
    "student": std,
    "teacher": Teacher(),
    "name": "Puja"
}
print(data.keys())
print(data.values())
print(data.items())

print(data['name'])
print(data['student'])

data['new_field'] = "This is a new field"

print(data)

for key, value in data.items():
    print("Data for {} is {}".format(key, value))
    print("Data for " + str(key) + " is " + str(value))
    # print(f"Data for {key} is {value}")

