def PasswordVerfication(pwdList):
    num = len([x for x in pw if isinstance(x, str)])
    u = 0   #upper
    l = 0   #lower
    s = 0   #special
    d = 0   #digit
    Vpw = []
    Ipw = []
    count1 = 0
    while count1 < num:
        if (len(pw[count1]) >= 8):
            for i in pw[count1]:
                if (i.islower()):
                    l+=1
                if (i.isupper()):
                    u+=1
                if (i.isdigit()):
                    d+=1
                if(i=='@'or i=='$' or i=='!' or i == '#' or i == '%'):
                    s+=1
            if (l>=2 and u>=2 and s>=1 and n>=1 and l+s+u+n==len(s)):
                Vpw.append(pw[count1])
            else:
                Ipw.append(i)
        count1+=1
        return Vpw,Ipw
pw = [x for x in input("Enter password list: ").split(";")]
num = len([x for x in pw if isinstance(x, str)])
count = 0
print('==========================================')
print('Entered passwords include:')
while count < num:
    print(pw[count])
    count+=1
print('==========================================')
V, B = PasswordVerfication(pwdList)
print('Verified passwords include: ')
print(V)
print('==========================================')
print('Bad passwords include: ')
print(B)