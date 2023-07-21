#6511171_Wai_Yan_Paing_542_class_12_No_1
def convertion(b_num,d_num):
    for j in b_num:
        if int(j) == 0:
            print(f'The input cannot start with 0.')
        for i in range(len(b_num)):
            temp = b_num.pop()
            if temp == '1':
                d_num = d_num + pow(2, i)
        return d_num
b_num = list(input("Input a binary number: "))
d_num = 0
print("The Integer Value is: ", convertion(b_num,d_num))