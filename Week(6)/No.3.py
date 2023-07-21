#6511171_Wai_Yan_Paing_542_class05_as4
numbers = []
lowest_number = numbers[0]
ans = numbers[0]
for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if ( numbers[i]>=numbers[j]):
            ans = numbers[i]-numbers[j]
        elif(numbers[i]<=numbers[j]):
            ans = numbers[j]-numbers[i]
        if(ans < lowest_number):
            lowest_number=ans
        else:
            ans=lowest_number
print("The lowest different between two numbers is ", lowest_number)