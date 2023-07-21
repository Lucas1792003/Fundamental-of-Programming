#section542_Q(no.1)_6511171
mylist = input('Enter words: ')
x = [str(x) for x in mylist.split(" ")]
vowels = ('a', 'e', 'i','o','u','A','E','I','O','U')
newlist = ""
newslist = ""
for y in x:
    for i in range(len(y)):
            if y[i] not in vowels:
               newlist+= y[i]
    newlist+=" "
print(f'Out put 1 = ',newlist)
sen = newlist.split(' ')
count = 0
while count < len(sen):
    if len(sen[count]) < 3:
        if len(sen[count]) == 1:
            newslist += '*'
        elif len(sen[count]) == 2:
            newslist += '**'
    elif len(sen[count])>= 3:
        newslist += sen[count]
    newslist += ' '
    count+=1
print(f'Out put 2 = ',newslist)