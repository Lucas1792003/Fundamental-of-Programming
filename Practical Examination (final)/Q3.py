
def keepCenter2or3(list):
    middle = len(list)//2
    if len(list)> 3: 
        if len(list) % 2 != 0:
            ans = list[(middle -1):middle+2]
            return ans
        else:
            ans = list[(middle -1):middle+1]
            return ans
    else:
        return list
list = [1,82,6,9,2]
list1 = [1,2]
list2 = [85,6,76]
list3 = [1,2,3,4,5,6,7,8,9]
list4 = [1,3,5,7,9]
print(f'First_message: ', keepCenter2or3(list))
print(f'Second_message: ', keepCenter2or3(list1))
print(f'Third_message: ', keepCenter2or3(list2))
print(f'Fourth_message: ', keepCenter2or3(list3))
print(f'Fifth_message: ', keepCenter2or3(list4))
