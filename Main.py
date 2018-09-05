# Task 2:
print()
print("Hello world")
print('-' * 50)


# Task 3:
def dividable(a: int, b: int):
    if a < 0 or b < 0:
        print("One of numbers are less than 0")

    returnable = True

    if a > b:
        if a % b != 0:
            returnable = False

    else:
        if b % a != 0:
            returnable = False

    return returnable


print(dividable(5, 3))
print(dividable(3, 6))
print('-' * 50)


array = []


# Task 4:
def arrayLine(a, b):
    if type(a) is int and type(b) is int:

        if a < b:
            for i in range(0, b - a):
                array.append(a + i)

        elif a > b:
            for i in range(0, a - b):
                array.append(b + i)

        else:
            array.append(a)
            return array

    else:
        print("NoSimpleDigits error")


arrayLine(10, 3.6)
print(arrayLine(0, 12))
print('-' * 50)


# Task 5:
def arrayOrganizer(chaosArray):
    for i in range(0, len(chaosArray)):
        if isinstance(chaosArray[i], list):
            arrayOrganizer(chaosArray[i])
        else:
            array.append(chaosArray[i])
    return array


print(arrayOrganizer(['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]))
