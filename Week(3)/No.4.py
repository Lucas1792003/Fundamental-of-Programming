#6511171_Wai_Yan_Paing_542_class03_as4
num = int(input("Enter 5-digits number: "))
firstnum = num // 10000
s_digit = num % 10000
t_digit = num % 1000
f_digit = num % 100
secondnum = s_digit // 1000
thirdnum = t_digit // 100
fourthnum = f_digit //10
lastnum = f_digit % 10
s = firstnum + secondnum  + fourthnum + lastnum
if num <= 9999:
    print("Worng Input. Try Again.")
elif thirdnum > s:
    print(str(lastnum) + str(secondnum) + str(thirdnum) + str(fourthnum) + str(firstnum))
elif thirdnum < s:
   print(str(firstnum) + str(fourthnum) + str(thirdnum) +str(secondnum) + str(lastnum))
else:
    print(num)
