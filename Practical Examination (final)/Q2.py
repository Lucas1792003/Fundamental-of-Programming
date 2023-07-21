#6511171_Wai_Yan_Paing_Final_Q2
def unHiddenMessage(inStr):
    count1 = 1
    count2 = 3
    ans = ''
    while count1 < len(inStr):
        ans+=inStr[count1]
        count1 += count2
        count2+=2
    return ans
First_message = unHiddenMessage('0F23i5678n012345a78901234l')
Second_message = unHiddenMessage('0W23E5678L012345P78901234!67890')
Third_message = unHiddenMessage('ayjwoeasdyalksdoko')
Fourth_message =unHiddenMessage('0a2sb4ws5c7rsa89d12')
Fifth_message = unHiddenMessage('qe2eaqcvt')
print(f'First_message: ', First_message)
print(f'Second_message: ', Second_message)
print(f'Third_message: ', Third_message)
print(f'Fourth_message: ', Fourth_message)
print(f'Fifth_message: ', Fifth_message)