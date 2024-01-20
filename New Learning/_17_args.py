#*args  allows us to take multiple input as a tuple
#we also use other keyword in place of args (only * matters)
#by convenstion we use args
def add_num(*args):
    return sum(args)

print(add_num(12,3,4,5,3,5,5,3,3,3,3))
