#range()

for i in range(5):
    print(i)

print("----")

#range(start,end,step size)
for i in range(2,10,2):
    print(i)

print("-----")

#generate list
print(list(range(0,11,2)))



#enumerate (index_count, value)

w="abcdefgh"
for i in enumerate(w):
    print(i)

print("---")

for index,value in enumerate(w):
    print(index)
    print(value)
    print('\n')


#zips - zip together 2 or more  list

lst1 =[1,23,4]
lst2=['a','b','c']

for i in zip(lst1,lst2):
    print(i)


# in
print(2 in [1,2,3,4])

print('k' in {'k':23})

d ={'k1':345}

print(345 in d.values())
print(345 in d.keys())

#max
print(max(lst1))
print(min(lst2))

