num = int(input("Enter 3-digit numbers: "))
x = num % 10
y = (num % 100)//10
z = num // 100
num_2 = x,y,z
print(x,y,z)
print(f'The new number is {num_2}.')