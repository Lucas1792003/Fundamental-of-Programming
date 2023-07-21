#6511171_Wai_Yan_Paing_542_class05_as05
numberA= [1, 52,36, 25, 8, -12]
numberB = [3, -54, 232, 4, 76, 340]
num = numberA + numberB
lowest_number = num[0]
ans = num[0]
for i in range(len(num)-1):
    for j in range(i+1, len(num)):
        if ( num[i]>=num[j]):
            ans = num[i]-num[j]
        elif(num[i]<=num[j]):
            ans = num[j]-num[i]
        if(ans < lowest_number):
            lowest_number=ans
        else:
            ans=lowest_number
print("The lowest different between two numbers is ", lowest_number)