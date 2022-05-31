
def romanToInt(inString: str) -> int:
    romanSum = 0

    for i in range(len(inString)):

        if i > 0:
            if inString[i] == 'M' and inString[i-1] == 'C' or inString[i] == 'D' and inString[i-1] == 'C':
                romanSum -= 200
            elif inString[i] == 'C' and inString[i-1] == 'X' or inString[i] == 'L' and inString[i-1] == 'X':
                print(inString[i-1])
                romanSum -= 20
            elif inString[i] == 'X' and inString[i-1] == 'I' or inString[i] == 'V' and inString[i-1] == 'I':
                romanSum -= 2

        match inString[i]:
            case 'M':
                romanSum += 1000
            case 'D':
                romanSum += 500
            case 'C':
                romanSum += 100
            case 'L':
                romanSum += 50
            case 'X':
                romanSum += 10
            case 'V':
                romanSum += 5
            case 'I':
                romanSum += 1
        print(romanSum)

    return romanSum


print(romanToInt('MCMXCIV'))

# 1000 + 900 +