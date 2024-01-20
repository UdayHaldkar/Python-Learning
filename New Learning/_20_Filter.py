#similar to map(), map applies function to every single element
#on other hand filter() - Filter based on the function condition


def check_even(num):
    return num%2==0

mynum =[2,31,44,56,76,6,5,9]

print(list(filter(check_even,mynum)))

#or

for i in filter(check_even,mynum):
    print(i)



#By using Lambda

evens = list(filter(lambda n: n%2 == 0, mynum))

print(evens)

