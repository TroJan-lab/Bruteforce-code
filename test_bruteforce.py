#word_generated=[]
li_iter1=[]
li_iter2=[]
li_iter3=[]
li_iter4=[]
in1=str(input(('enter guessed letters (only 4 digits)-')))
for i in in1:
    li_iter1.append(i)
for j in in1:
    for x in li_iter1:
        c=j+x
        li_iter2.append(c)
for k in in1:
    for y in li_iter2:
        c1=k+y
        li_iter3.append(c1)
for l in in1:
    for z in li_iter3:
        c2=l+z
        li_iter4.append(c2)
count=0
for i in li_iter4:
    count+=1
    print(i,end=',')

print('\n\nTotal bruteforce-',count)
print('\n\n')
