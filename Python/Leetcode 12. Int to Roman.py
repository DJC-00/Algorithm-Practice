
def intToRoman(inputInt):
    run = True
    letterCount = {}
    resString = ""
    remainder = 0

    while run == True:
        if inputInt >= 1000:
            remainder = inputInt % 1000
            count = (inputInt - remainder) / 1000
            inputInt = remainder
            letterCount.update({'M':count})

        elif inputInt >= 900:
            remainder = inputInt % 900
            count = (inputInt - remainder) / 900
            inputInt = remainder
            letterCount.update({'CM':count})

        elif inputInt >= 500:
            remainder = inputInt % 500
            count = (inputInt - remainder) / 500
            inputInt = remainder
            letterCount.update({'D':count})

        elif inputInt >= 400:
            remainder = inputInt % 400
            count = (inputInt - remainder) / 400
            inputInt = remainder
            letterCount.update({'CD':count})

        elif inputInt >= 100:
            remainder = inputInt % 100
            count = (inputInt - remainder) / 100
            inputInt = remainder
            letterCount.update({'C':count})

        elif inputInt >= 90:
            remainder = inputInt % 90
            count = (inputInt - remainder) / 90
            inputInt = remainder
            letterCount.update({'XC':count})

        elif inputInt >= 50:
            remainder = inputInt % 50
            count = (inputInt - remainder) / 50
            inputInt = remainder
            letterCount.update({'L':count})

        elif inputInt >= 40:
            remainder = inputInt % 40
            count = (inputInt - remainder) / 40
            inputInt = remainder
            letterCount.update({'XL':count})

        elif inputInt >= 10:
            remainder = inputInt % 10
            count = (inputInt - remainder) / 10
            inputInt = remainder
            letterCount.update({'X':count})

        elif inputInt >= 9:
            remainder = inputInt % 9
            count = (inputInt - remainder) / 9
            inputInt = remainder
            letterCount.update({'IX':count})

        elif inputInt >= 5:
            remainder = inputInt % 5
            count = (inputInt - remainder) / 5
            inputInt = remainder
            letterCount.update({'V':count})

        elif inputInt >= 4:
            remainder = inputInt % 4
            count = (inputInt - remainder) / 4
            inputInt = remainder
            letterCount.update({'IV':count})

        else:
            if inputInt > 0:
                letterCount.update({'I':inputInt})
            run = False

    for letter, num in letterCount.items():
        resString+=(letter * int(num))

    return resString





# myInt = 1092
# remainder = (myInt%40)
# print((myInt-remainder)/40, remainder)

print(intToRoman(400))
print ('x'*7)