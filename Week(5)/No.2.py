#6511171_Wai_Yan_Paing_542_class05_as2
for i in range (0,31):
    if i % 3 == 0:
        if not (( i > 9 and i < 16) or ( i > 19 and i < 26)):
            print(i, end = '')
        else:
            print(f'_', end = '')
    elif not (( i > 9 and i < 16) or ( i > 19 and i < 26)):
        print(f'*', end = '')
    else:
        print(f'_', end = '')