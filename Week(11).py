#6511171_Wai_Yan_Paing_class10_section542_as1
def split_type(numlist):
    temp_int=[]
    temp_float=[]
    for temp in numlist:
        if isinstance(temp,int)==True:
            temp_int.append(temp)
        else:
            temp_float.append(temp)
    return temp_int,temp_float

def ListOfOdd(numlist):
    if not numlist:
        return []
    if numlist[0] % 2 == 1:
        return [numlist[0]] + ListOfOdd(numlist[1:])
    return ListOfOdd(numlist[1:])

def keeptwodump(numlist):
    temp=[]
    for i in numlist:
        if  i not in temp:
            temp.append(i)
        elif i in temp:
            count=0
            for j in temp:
                if j==i:
                    count+=1
            if count < 2:
                temp.append(i)      
    return temp
def main():
    numlist=[1,2,2,2,3,4,5,5,5,1,2,3,3]
    print("split_type=",split_type(numlist))
    print("ListOfOdd=",ListOfOdd(numlist))
    print("keeptwodump",keeptwodump(numlist))
main()