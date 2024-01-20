
f = open('My_Data.txt','r') #r -read

print(f)

print(f.read())

f1=open('data2','r')

f2 = open('abc','w') # create a new file w- write, a- append , rb - read binary
f2.write("hello There")
f2.write(" Hi everyone")



#Copy and access images

i1 =open('valo.jpeg','rb')

i2 =open('imgg.jpeg', 'wb')  #Write binary

for i in i1:
    i2.write(i)




#copy all the data of "My_data" to "abc"

for d in f:
    f2.write(d)