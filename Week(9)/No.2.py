#6511171_class09_542_as2
n_list = [[2,5,99,99], [-3,8,1,2,10], [1, 7,100,10]]
even_list = [[num for num in l if num%2 == 0] for l in n_list]
odd_list = [[num for num in l if num%2 == 1] for l in n_list]
print(f'Output: even_list = ',even_list) 
print(f'Output: odd_list = ',odd_list)     