#6511171_Wai_Yan_Paing_541_class08_ans2.1
x = [str(x) for x in input("Input: ").split()]
print("List: ", x)
ans = " "
count = 0
while len(x)> count :
    count2 =count+1
    while len(x)> count2:
        if x[count]==x[count2] :
            x.pop(count2) 
            count2-=1
        count2+=1
    count+= 1
for i in x:
    ans += i +' '
print(f'Output:',ans)