#6511171_Wai_Yan_Paing_542_class05_as1.2
#(b)
for i in range (1, 10):
    for j in range (1,10):
        if ((i*j) % 2) == 0 and (((i*j)%10) % 2) == 0 and (((i*j)//10) % 2) == 0:
            print(f'{i*j:2d}', end = ' ')
        else:
            print(f'--', end = ' ')
    print()
    


# Just in case, 'Zero' not consider as a even number.

#for i in range (1, 10):
    #for j in range (1,10):
        #if ((i * j)% 10)!= 0 and ((i*j) % 2) == 0 and (((i*j)%10) % 2) == 0 and (((i*j)//10) % 2) == 0:
            #print(f'{i*j:2d}', end = ' ')
        #else:
            #print(f'--', end = ' ')
    #print()