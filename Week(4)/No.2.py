#6511171_Wai_Yan_Paing_542_class04_as2
num = int(input('Input number: '))
snum = 0
while num > 0:
    x = num % 10
    snum = x + snum * 10
    num = num // 10
print(f'Output Number: ', snum) 