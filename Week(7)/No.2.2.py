#6511171_Wai_Yan_Paing_541_class08_ans2.2
#Another_way_of_solving_Q(2)
x = [str(x) for x in input("Input: ").split()]
fans = ''
ans = list(dict.fromkeys(x))
for i in ans:
    fans += i +' '
print(f'Output:',fans)