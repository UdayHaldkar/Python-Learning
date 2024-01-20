#in map() if we pass the function we want to map every single item/element


def sqr(num):
    return num**2

my_num=[1,3,5,7,9]

for i in map(sqr,my_num):
    print(i)

    #or
print(list(map(sqr,my_num)))


#By using lambda

square = list(map(lambda n : n*n,my_num))

print(square)