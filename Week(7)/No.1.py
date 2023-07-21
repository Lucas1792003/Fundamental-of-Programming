#6511171_Wai_Yan_Paing_541_class08_ans1
x = [str(x) for x in input("Enter words: ").split()]
print("List: ", x)
count = 0
ans=0
while len(x)>count and len(x[count]) >= 4:
    if x[count][0]==x[count][-1]:
        ans +=1
    count+= 1
print('Number of words that meets the requirements is: ',ans)