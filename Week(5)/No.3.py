#6511171_Wai_Yan_Paing_542_class05_as3
a = int(input('Enter int_1: '))
b = int(input('Enter int_2: '))
for i in range(a,b):
    if not ((i % 10 == 3) or (i % 10 == 7)):
        if ((i%10)+ (i//10))<8:
            print(i, end = ' ')
        elif not ((i % 10 == 3) or (i % 10 == 7)):
            print(f'%', end = ' ')
        else:
            print(f'*', end = ' ')     
    else:
        print(f'*', end = ' ')

    