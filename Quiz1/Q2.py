
mylist = input('Enter number(s) separated by space: ')
x = [int(x) for x in mylist.split(" ")]
x.remove(max(x))
x.remove(min(x))
y = x
avg = sum(y)/len(y)
print (f'The average of number(s) in list excluding highest and lowest is ',avg)


