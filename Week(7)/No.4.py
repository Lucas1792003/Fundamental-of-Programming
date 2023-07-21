#6511171_Wai_Yan_Paing_542_class08_ans4
x = [str(x) for x in input("Input: ").split()]
print("List: ", x)
n = int(input('Enter a value for n: '))
ans = ' '
count = 0
num = 1
while len(x)> count :
    num = 1
    while num <= n:
        if num % 2 == 0:
            x[count]=x[count].upper()
        else:
            x[count]=x[count].lower()
        ans += x[count] + str(num) + ' '
        num+=1
    count+=1
print(ans)