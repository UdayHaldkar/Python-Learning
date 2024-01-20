# {'key1':'value1','key2':'value2'}

my_dict= {'name':'Uday', 'Last':'Haldkar'}
print(my_dict)
print(my_dict['name'])

#dict can hold list and tuples
d={'k1':123,'k2':[0,1,2],'k3':{'insideKey':100},'k4':['a','d','r']}
print(d)
print(d['k3'])
print(d['k3']['insideKey'])

print(d['k2'][1])

print(d['k4'][2])
print(d['k4'][2].upper())

d['k5']=3000

d['k1']="hello"
print(d)
print(d['k5'])