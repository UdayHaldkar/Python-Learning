import sys

print(sys.getrecursionlimit())


sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())

#Finding Factorial using recursion
def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

print(fact(5))