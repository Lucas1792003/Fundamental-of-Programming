#6511171_Wai_Yan_Paing_541_class_12_no_2&3
def rigtAndRight(sen, shift, direction):
    if(direction=='r'):
        return easyED(sen, shift, direction)
    else:
        return easyDE1(sen, shift, direction)

def easyED(sen, shift, direction):
    baseLower = ord('a')
    baseUpper = ord('A')
    ciphertext = ''  
    for c in sen:
            if c.isupper():
                newc = (ord(c) - baseUpper + shift) % 26
                ciphertext += chr(newc + baseUpper)
            elif c.islower():
                newc = (ord(c) - baseLower + shift) % 26
                ciphertext += chr(newc + baseLower)
        
            else:
                ciphertext += c
    return ciphertext  
def easyDE1(ciphertext, shift, direction):
        baseLower = ord('a')
        baseUpper = ord('A')
        originaltext = ''
        for c in ciphertext:
            if c.isupper():
                newc = (ord(c) - baseUpper - shift) % 26
                originaltext += (chr(newc + baseUpper))
            elif c.islower():
                newc = (ord(c) - baseLower - shift) % 26
                originaltext += (chr(newc + baseLower))
            else:
                originaltext +=c
        return originaltext
sen = input("Enter the message you want to encrypt: ")
shift  = int(input("Enter the number you want to shift by: "))       
ans1=rigtAndRight(sen, shift, 'r')
print("Encrypted Text for right-wise is: ",ans1)
ans2=rigtAndRight(ans1, shift, 'l')
print("Decrypted Text is: ",ans2)
ans3=rigtAndRight(sen, shift, 'l')
print("Encrypted Text for left-wise is: ",ans3)