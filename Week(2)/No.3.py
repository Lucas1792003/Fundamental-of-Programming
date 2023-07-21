area_size = int(input("Enter an area size in square_meter: "))
area_1 = area_size*1550.0031
area_2 = area_1*0.00694444
area_3 = area_size//1000000
print(f'The area size in square-inch is {area_1}.')
print(f'The area size in square-feet is {area_2}.')
print(f'The area size in square-km is {area_3}.')
