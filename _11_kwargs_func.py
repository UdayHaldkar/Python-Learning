def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("My Fruit is {}".format(kwargs['fruit']))
    else:
        print("i did not find any fruit")


myfunc(fruit='apple', veggie='tomato')

#combination of args and kwargs

def myfun(*args,**kwargs):
    print(args)
    print(kwargs)
    print("I would like to {} {}".format(args[0],kwargs['food']))


myfun( 10,30,20,fruit='orange',food='eggs',animals='dog')