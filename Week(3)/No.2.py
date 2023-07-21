#6511171_Wai_Yan_Paing_542_class03_as2
x = int(input("Enter the first number: "))
x1 = int(input("Enter the second number: "))
x2 = int(input("Enter the third number: "))
x3 = int(input("Enter the fourth number: "))
s = x + x1 + x2 + x3

if s % 2 == 0 and s > 0:
    print(F'{s} is Positive Even.')
elif s > 0 and s % 2 == 1:
    print(f'{s} is Positive Odd.')
elif s < 0 and s % 2 == 0:
    print(f'{s} is Negative Even.')
elif s < 0 and s % 2 == 1:
    print(f'{s} is Negative Odd.')
elif s == 0:
    print(f'{s} is Zero.')