def PasswordVerification(pwList):
    Vpw = []
    Ipw = []

    for pw in pwList:
        num = len(pw)
        u = 0   # upper
        l = 0   # lower
        s = 0   # special
        d = 0   # digit

        if num >= 8:
            for i in pw:
                if i.islower():
                    l += 1
                if i.isupper():
                    u += 1
                if i.isdigit():
                    d += 1
                if i in ['@', '$', '!', '#', '%']:
                    s += 1

            if l >= 2 and u >= 2 and s >= 1 and d >= 1 and l + s + u + d == num:
                Vpw.append(pw)
            else:
                Ipw.append(pw)

    return Vpw, Ipw

pwList = input("Enter password list separated by semicolons: ").split(";")

print('==========================================')
print('Entered passwords include:')
for pw in pwList:
    print(pw)
print('==========================================')

V, B = PasswordVerification(pwList)

print('Verified passwords include:')
print(V)
print('==========================================')

print('Bad passwords include:')
print(B)
