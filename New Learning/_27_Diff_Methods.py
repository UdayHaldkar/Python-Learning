from numpy import *

arr1 =array([
    [1,2,3],
    [4,5,6]
]

)
#shape =number of row and column
print(arr1.shape)

print(arr1.size)

#convert 2d array to 1d array
print(arr1.flatten())

#convert  1d to 2d array

arr3= arr1.reshape(2,3)
print(arr3)


print("\n")
#creating martrix

m=matrix('1 2,3 ; 4,5,6 ; 7,8,9')
m2 =matrix('2,3,4 ;5,3,5 ; 8,2,4')

print(m)

print("\n")

m3 =m+m2
print(m3)

print("\n")

print(m*m2)