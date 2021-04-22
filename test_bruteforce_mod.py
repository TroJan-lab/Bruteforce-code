in_1=list(input('Enter character-'))
in_2=str(input('Enter number to search-'))

li_bruteforce=[]
li_temp=in_1

for k in li_temp:
    for l in in_1:
        li_bruteforce.append(k+l)
    if in_2 in li_bruteforce:
        print('found at index-',li_bruteforce.index(in_2))
        print('\n\n',li_bruteforce[li_bruteforce.index(in_2)])
        break

for i in range(len(in_1)-2):
    temp=[]
    for x in li_bruteforce:
        for y in in_1:
            temp.append(x+y)
    li_bruteforce=temp
    if in_2 in li_bruteforce:
        print('found at index-',li_bruteforce.index(in_2))
        print('\n\n',li_bruteforce[li_bruteforce.index(in_2)])
        break

print(li_bruteforce)
print('/n',len(li_bruteforce))

