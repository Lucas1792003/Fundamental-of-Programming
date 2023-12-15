
zeroCount = 0
total = 0
oddList = []
evenList = []
while True:
    try:
        myNum = int(input('Enter an integer: '))
    except ValueError:
        print('==================================')
        print("Not an integer! Try again.")
        print('==================================') 
        continue
    else:
        if myNum != 0 and myNum % 2 == 0 :
            evenList.append(myNum) 
            evenList.sort()
        elif myNum != 0 and myNum % 2 != 0:
            oddList.append(myNum)
            oddList.sort()
        total += myNum
    if myNum == 0:
        zeroCount+=1
        if zeroCount == 3:
            break
print(f'Total is {total}.')
print(f'Oddlist {oddList}.')
print(f'Evenlist {evenList}.')
