import json

class control:
    def __init__(self):
        self.generalInfo = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                                     "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                                     "V", "W", "X", "Y", "Z"]

        self.booleanExpression = {}
        self.amountOfVariables = 0
        self.letterStart = "    "
        self.decimalNumber = 0

    def creator(self):
        self.amountOfVariables = int(input("Choose amount of variables: "))

        self.letters()

        self.dividerLines(len(self.letterStart))

        for i in range(0, 2 ** self.amountOfVariables):
            self.decimalNumber = i
            binary = self.binaryToDecimal()

            print(f"| {i} {binary} ")
            self.dividerLines(len(self.letterStart))
            # self.booleanExpression[i] = binary

        self.writter()

    def letters(self):

        for i in range(0, self.amountOfVariables):
            self.letterStart += f"| {self.generalInfo[i]} "

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

    def dividerLines(self, amountVar):
        amount = int(amountVar)
        dividerLine = "-" * amount

        print(dividerLine)

create = control()

create.creator()