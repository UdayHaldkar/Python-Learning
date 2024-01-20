# array package in python don't have 2D array so have to help of others packages

from numpy import *

arr =array([1,3,2,45,6,4,3])
print(arr)

#differents ways of creating arrays by numpy
# array() , linspace(), logspace(), arange(), zeros(), ones()

val =linspace(1,16,4)  #start, stop,no.of path



print(val)

mar =arange(1,15,3) #start , stop, steps



arr3 =arr+5
print(arr3)

arr4 =arr+ arr3

print(arr4)

print(sqrt(arr))

print(sum(arr))
print(min(arr))
print(max(arr))
print(sort(arr))