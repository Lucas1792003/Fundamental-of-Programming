#6511171_class09_542_as1
List_1 = [1, 4]
List_2 = [3,6,7,4]
ans=""
if len(List_1) < len(List_2):
    if len(list(set(List_1)-set(List_2)))==0:
        print("Yes List_1 is a subset of List_2")
    else:
        print("No") 
else:
    if len(list(set(List_2)-set(List_1)))==0:
        print("Yes List_2 is a subset of List_1")
    else:
        print("No") 