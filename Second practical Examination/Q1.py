#6511171_Wai_Yan_Paing_Final_Q1
def Transaction(strinput):
    balance = 1000
    if 'W' == strinput[0]:
        if int(strinput[2:]) < balance:
            print(f'{int(strinput[2:])} has been withdrawn from your account.')
            return balance - int(strinput[2:])
        else:
            print('Not enough money!')
    elif 'D' == strinput[0]:
        print(f'{int(strinput[2:])} has been deposited to your account.')
        return balance + int(strinput[2:])
    
    elif 'S' == strinput[0]:
        print(f'You have {balance} USD in your account.')
        return balance
    elif strinput[2] == ' ':
        print('Invalid Transaction')
    
strinput = input('Enter input: ')
balance = 1000

balance = (Transaction(strinput))