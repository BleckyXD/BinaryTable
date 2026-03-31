import json

class control:
    def __init__(self):
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                                     "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                                     "V", "W", "X", "Y", "Z"]

        self.negatedLetters = ["Ā", "B̄", "C̄", "D̄", "Ē", "F̄", "Ḡ", "H̄", "Ī", "J̄", "K̄",
                          "L̄", "M̄", "N̄", "Ō", "P̄", "Q̄", "R̄", "S̄", "T̄", "Ū",
                          "V̄", "W̄", "X̄", "Ȳ", "Z̄"]

        self.booleanExpression = {}
        self.amountOfVariables = 0
        self.letterStart = "    "
        self.decimalNumber = 0

    def creator(self):
        self.amountOfVariables = int(input("Choose amount of variables: "))

        self.startLetters()

        self.dividerLines()

        for i in range(0, 2 ** self.amountOfVariables):
            self.decimalNumber = i
            binary = self.binaryToDecimal()

            print(f"| {i} {binary} ")
            self.dividerLines()
            # self.booleanExpression[i] = binary

        self.writter()
        self.SOPcreator()

    def SOPcreator(self):
        # booleans = []
        # with open("information.json", "r") as f:
        #     booleans = list(json.load(f).values())
        # booleans = list(self.booleanExpression.values())

        SOPexpression = []
        for value in list(self.booleanExpression.values()):
            sop = ""
            # print(value)
            list(value)
            for i, num in enumerate(value):
                if num == "1":
                    sop += f"{self.letters[i]}"

                else:
                    sop += f"{self.negatedLetters[i]}"
            SOPexpression.append(sop)

        finalSOP = " + ".join(SOPexpression)
        print(finalSOP)

    def startLetters(self):

        for i in range(0, self.amountOfVariables):
            self.letterStart += f"| {self.letters[i]} "

        self.letterStart += "|"
        print(self.letterStart)

    def writter(self):
        with open("information.json", "w") as f:
            json.dump(self.booleanExpression, f, indent=4)

    def binaryToDecimal(self):
        num = ""
        zeroCheck = self.decimalNumber
        newKey = self.decimalNumber

        while (self.decimalNumber != 0):
            num += str(self.decimalNumber % 2)
            self.decimalNumber = int(self.decimalNumber / 2)

        while (len(num) % self.amountOfVariables != 0):
            num += "0"

        if (zeroCheck == 0):
            for i in range(0, self.amountOfVariables):
                num += "0"

        num = num[::-1]
        self.booleanExpression[newKey] = num

        completed = ""
        for digit in num:
            completed += f"| {digit} "

        completed += "|"

        return completed

    def dividerLines(self):
        amount = int(len(self.letterStart))
        dividerLine = "-" * amount

        print(dividerLine)

#create = control()
#create.creator()

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                                     "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                                     "V", "W", "X", "Y", "Z"]
with open("information.json", "r") as f:
    booleans =json.load(f)



y = list(booleans.values())
length = 4

listA = []
resultA = []

listB = []
resultB = []

if length % 2 == 0:
    for value in y:
        x = list(value)
        firstPart = ""
        secondPart = ""

        for i in range(0, length // 2):
            firstPart += x[i]
        listA.append(firstPart)

        for i in range(length - 1, length // 2 - 1, -1):
            secondPart += x[i][::-1]

        send = secondPart[::-1]
        listB.append(send)

# number = (list("1110"))[::-1]
# result = 0
#
# for i in range(0, len(number)):
#     result += (2 ** i) * int(number[i])

# print(result)

for i in listA:
    number = (list(i))[::-1]
    result = 0

    for i in range(0, len(number)):
        result += (2 ** i) * int(number[i])
    #print(result)
    resultA.append(result)

for i in listB:
    number = (list(i))[::-1]
    result = 0

    for i in range(0, len(number)):
        result += (2 ** i) * int(number[i])
    resultB.append(result)

for i in range(0, len(resultA)):
    print(f"A = {resultA[i]} | B = {resultB[i]}")
    if int(resultA[i]) > int(resultB[i]):
        print("A IS HIGHER THAN B")
    elif int(resultA[i]) < int(resultB[i]):
        print("B IS HIGHER THAN A")

    elif int(resultA[i]) == int(resultB[i]):
        print("A AND B ARE EQUAL")


print(resultA)
print(resultB)
#print(listB)
# print(listA)

#Binary to Decimal

# for value in listA:
#     x= 0
#     value = list(value)
#
#     for i, digit in enumerate(value):
#         x += 2 ** (length // 2 - i) * int(digit)

# for value in listA:
#     value = list(value)
#     x = 0
#     for i in range (0, len(value)):
#         print(value[i])
#         x += (2 ** i) * int(value[i])
#
# for i in listA:
#     print(i)
#


#def BinaryToDecimal():
    #num = "1110"

    #length = len(num)
    # num = list(num)
    # num = num[::-1]


#BinaryToDecimal()