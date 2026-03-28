import json

generalInfo = {"Abecedary": [ "A","B","C","D","E","F","G","H","I","J","K",
                              "L","M","N","O","P", "Q", "R", "S", "T","U",
                              "V","W","X","Y", "Z"]}

booleanExpression = {}

def binaryToDecimal(binary, tableLength):
    num = ""
    zeroCheck = binary


    while(binary != 0):

        num += str(binary % 2)
        binary = int(binary / 2)

    while(len(num) % tableLength != 0):
        num += "0"

    if (zeroCheck == 0):
        for i in range(0, tableLength):
            num += "0"


    num = num[::-1]


    print(num)
    list(num)

    completed = ""
    for digit in num:
        completed += f"| {digit} "
    completed += "|"
    return completed

def dividerLines(amountVar):
    amount = int(amountVar)
    dividerLine = "-" * amount


    print(dividerLine)

amountOfVariables = int(input("Choose amount of variables: "))

letterStart = "    "
for i in range(0, amountOfVariables):

    letterStart += f"| {generalInfo["Abecedary"][i]} "

letterStart += "|"
print(letterStart)

dividerLines(len(letterStart))



for i in range(0, 2**amountOfVariables):
    binary = binaryToDecimal(i, amountOfVariables)

    print(f"| {i} {binary} ")
    dividerLines(len(letterStart))
    booleanExpression[i] = binary

generalInfo["booleans"] = booleanExpression

with open("information.json", "w") as f:
    json.dump(generalInfo, f, indent= 4)


