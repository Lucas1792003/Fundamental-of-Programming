#6511171_Wai_Yan_Paing_542_class04_as1
n = int(input('Enter number of real number: '))
first_highest_num = 0
second_highest_num = 0
i = 1
while i <= n:
    num = float(input(f'Number#{i}: '))
    i += 1
    if first_highest_num < num:
        second_highest_num = first_highest_num
        first_highest_num = num
    elif second_highest_num < num:
        second_highest_num = num
print(f'The first hightest number is { first_highest_num}.')
if n == 1:
    print(f'There is no second highest number.')
else:
    print(f'The second highest number is {second_highest_num}')