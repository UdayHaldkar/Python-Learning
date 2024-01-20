
def fac(n):
    if n<=1:
        print(1)

    factorial =1

    for i in range(1,n+1):

        factorial = factorial*i

    return factorial


print(fac(4))


