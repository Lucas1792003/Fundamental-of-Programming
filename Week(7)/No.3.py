#6511171_Wai_Yan_Paing_542_class08_ans3
txt =input('Enter Input: ') 
y = txt.upper()
x = [str(x) for x in y.split()]
print("List: ", x)
n = int(input('Enter a value for n: '))
ans = ' '
count = 0
num = 1
while len(x)> count :
    num = 1
    while num <= n:
        ans += x[count] + str(num) + ' '
        num+=1
    count+=1
print(ans)