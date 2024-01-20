def say_hello():
    print("Hello")

say_hello()

def say_my_name(name):
    print(f'My name is {name}')

say_my_name("Uday")


#return

def add_nums(num1,num2):
    return num1+num2

print(add_nums(5,8))


#check even
mylist =[1,4,2,6,8]

def check_even(mylist):
    for i in mylist:
        if i%2==0:
            return True
        else:
            pass

    return False

print(check_even(mylist))