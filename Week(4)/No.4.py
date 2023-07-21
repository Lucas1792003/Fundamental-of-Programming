#6511171_Wai_Yan_Paing_542_class04_as4
numA = int(input('Enter numA: '))
numB = int(input('Enter numB: '))
finalnum = 0
if numA > numB:
    while numA >= numB:
        if finalnum > 5 * numA:
            break
        finalnum += numB
        if numB % 3 != 0 and numB % 7 != 0:
            print(numB) 
        numB += 1
if numA < numB:
    while numA<= numB:
        if finalnum > 5 * numB:
            break
        finalnum += numA
        if numA % 3 != 0 and numB % 7 != 0:
            print(numA)
        numA += 1
else:
    print(f'The value must be different. Please under different number.')


