#6511171_Wai_Yan_Paing_542_class06_as01
my_sen = input("Enter string: ")
uc = 0
lc = 0
sp = 0
rev = ""
for i in my_sen:
    if i.isupper():
        a = i.lower()
        uc += 1
        rev += a
    elif i.islower():
        a = i. upper()
        lc += 1
        rev += a
        print(a, end = "")
    else:
        sp += 1
        rev += " "
        print(i, end = "")

print(f'\n{uc} Uppercase\n{lc} Lowercase\n{sp} Spaces')
print(rev)