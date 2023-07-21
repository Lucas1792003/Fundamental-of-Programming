#6511171_Wai_Yan_Paing_542_class04_as3
count = 1
sumpos = 0
sumneg = 0
n = int(input(f'Number#{count}: '))
while n > 0:
    if n % 2 != 0:
        sumneg += n
        
    else:
        sumpos += n
    count = count + 1
    n = int(input(f'Number#{count}: '))
print(f'The sum of all odd numbers is: {sumneg}.')
print(f'The sum of all even number is: {sumpos}.')
if sumpos == sumneg:
    print(f'No winner here. Try again.')
elif sumpos < sumneg:
    print(f'The winner is the sum of all odd numbers.')
else:
    print(f'The winner is the sum of all even numbers.')