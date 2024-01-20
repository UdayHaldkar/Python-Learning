mylist =[]
mystr="hello"

for i in mystr:
    mylist.append(i)

print(mylist)

#or
mylist2=[]
mylist2=[letter for letter in mystr]

print(mylist2)

mylist3 =[x for x in 'worldd']
print(mylist3)

#celcius to frahenite

cel=[12,45,78,34]

fahrenhite =[((9/5)*temp+32) for temp in cel]

print(fahrenhite)
