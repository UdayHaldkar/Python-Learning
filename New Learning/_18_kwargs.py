# **kwargs takes multiple input as a  dictionary

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit is {}'.format(kwargs['fruit']))
    else:
        print('no fruit')


myfunc(fruit='apple',veggie='cabbage')

#args and kwargs combine

def food(*args,**kwargs):
    print('i would like {} {}'.format(args[0],kwargs['food']))


food(10,23,54,food='eggs',animal ='dog')
