
# import array
#
# vals = array.array('i',[7,9,1,4,3,4])
#
# print(vals)


from array import *

vals = array('i',[1,2,3,7,9])

print(vals)
print(vals.buffer_info()) #size  array
print(vals.typecode)
print(vals.reverse())
vals.append(2)
print(vals)

print(vals[2])


#print each element
for i in vals:
    print([i])

for a in range(len(vals)):
    print(vals[a])
print("-----------------")
#take values from another array

newArr =array(vals.typecode,(a for a in vals))

for r in newArr:
    print(r)

print("\n")
#by while loop

i=0

while i<len(newArr):
    print(newArr[i])
    i+=1
