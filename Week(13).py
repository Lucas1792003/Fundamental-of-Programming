#6511171_542_class_13_wai_yan_paing
numlist = [int(x) for x in input("Enter multiple value: ").split(",")]
if len(numlist) < 4:
    print("Try again. List must have at least 4 elements.")
else:
    def linearSearch(numlist, key):
        count = 0
        while count < len(numlist):
            if numlist[count] == key:
                return True, count + 1
            count+=1
        return False, count
    def bidirectionSearch(numlist, key):
        count1 = 0
        count2 = len(numlist) - 1
        while count1 <= count2:
            if numlist[count1] == key or numlist[count2] == key:
                return True, count1 + 1
            count1 += 1
            count2 -= 1
        return False, count1
    def foursliceSearch(numlist, key):
        x = int(len(numlist)/4)
        ans, c1, c2, c3, c4 = 0, 0, 0, 0, 0
        for i in numlist:
            if numlist[:x][c1]==key or numlist[x:2*x][c2]==key or numlist[2*x:3*x][c3]==key or numlist[3*x:][c4]==key:
                ans +=1
                return True, ans
            c1+=1
            c2+=1
            c3+=1
            c4+=1
            return False, ans
    def fourslicebidirectionSearch(numlist, key):
        y = int(len(numlist)/4)
        a = 0
        b = len(numlist[:y])-1
        b1 =len(numlist[y:2*y])-1
        b2 =len(numlist[2*y:3*y])-1
        b3 =len(numlist[3*y:])-1
        for i in numlist:
            if (numlist[:y][a]==key or numlist[:y][b]==key ) or (numlist[y:2*y][a]==key or numlist[y:2*y][b1]==key) or (numlist[2*y:3*y][a]==key or numlist[2*y:3*y][b2]) or (numlist[3*y:][a]==key or numlist[3*y:][b3]==key):
                return True, a + 1
            a+=1
            b-=1
            b1-=1
            b2-=1
            b3-=1
        return False, a
key = int(input("Enter a number you want to search: "))
result, count = linearSearch(numlist,key)
result1, count1 = bidirectionSearch(numlist, key)
result2, count2 = foursliceSearch(numlist, key)
result3, count3 = fourslicebidirectionSearch(numlist, key)
print(f'LinearSearch: It takes {count} loops to find {key}.')
print(f'BidirectionSearch: It takes {count1} loops to find {key}.')
print(f'FoursliceSearch: It takes {count2} loops to find {key}.')
print(f'FourslicebidirectionSearch: It takes {count3} loops to find {key}.')