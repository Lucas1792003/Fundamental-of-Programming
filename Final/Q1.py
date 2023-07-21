def Transaction(strinput):
    global balance
    if 'W' == strinput[0]:
        if int(strinput[2:]) < balance:
            print(f'{int(strinput[2:])} has been withdrawn from your account.')
            balance -= int(strinput[2:])
        else:
            print('Not enough money!')
    elif 'D' == strinput[0]:
        print(f'{int(strinput[2:])} has been deposited to your account.')
        balance += int(strinput[2:])
    elif 'S' == strinput[0]:
        print(f'You have {balance} USD in your account.')
    elif strinput[2] == ' ':
        print('Invalid Transaction')

balance = 1000

while True:
    strinput = input('Enter input (type "exit" to quit): ')
    if strinput.lower() == 'exit':
        break
    Transaction(strinput)