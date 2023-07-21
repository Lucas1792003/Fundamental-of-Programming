#6511171_Wai_Yan_Paing_542_class03_as1
x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
x3 = int(input("Enter x3: "))
y = x1 % x3
y1 = x2 % x3
if y == 0 and y1 == 0:
    print(f'x3 is a factor of both x1 and x2.')
elif y == 0 and y1 != 0:
    print(f'x3 is a factor of x1.')
elif y1 == 0 and y != 0:
    print(f'x3 is a factor of x2.')
elif y != 0 and y1 != 0:
    print(f'x3 is neither a factor of x1 nor x2.')