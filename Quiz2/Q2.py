
def SumSkip37(numList):
    if len(numList) == 1:
        if numList[0] % 3 != 0 and numList[0] % 7 != 0:
            return numList[0]
        else:
            return 0
    else :
        if numList[0] % 3 != 0 and numList[0] % 7 != 0:
            return numList[0] +  SumSkip37(numList[1:])
        else:
            return  SumSkip37(numList[1:])
#numList = [int(numList) for numList in input("Enter multiple value: ").split(",")]
#numList = [1, 14, 4, 3, 28, 9, 10]
numList = [1, 3, 5, 7, 9]
print(f'The result is {SumSkip37(numList)}')
