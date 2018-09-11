# Task 1:
print("Task 1: \n" + ("-" * 60))
words = open("words.txt", "r").read()

def shortestWord():

    current = ''
    currentMin = 1000
    wordsList = words.split()

    for temp in wordsList:
        if len(temp) < currentMin:
            current = temp
            currentMin = len(temp)
    print(current)


shortestWord()
print("\nTask 2: \n" + ("-" * 60))


# Task 2:
poem = open("sadok.txt", "r").read()
lineList = poem.split("\n")
lineList = filter(None, lineList)

def evenLineUppercase():

    evenPoem = open("b1.txt", "w+")
    number = 1

    for string in lineList:
        if(number % 2 == 0):
            string = string.upper()
            evenPoem.write(string + "\n")

        number = number + 1


evenLineUppercase()


lineList = poem.split("\n")
lineList = filter(None, lineList)

def oddLineLowercase():

    oddPoem = open("b2.txt", "w+")
    number = 0

    for string in lineList:
        if (number % 2 == 0):
            string = string.lower()
            oddPoem.write(string + "\n")

        number = number + 1


oddLineLowercase()






