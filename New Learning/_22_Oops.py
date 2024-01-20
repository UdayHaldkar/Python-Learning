# class NameOFClass():
#
#     def __init__(selfself,param1,param2):
#         self.param1 =param1
#         self.param2 =param2
#
#
#     def some_method(self):
#         #perfom some action
#         print(self.param1)


class SampleWorld():
    pass

print(type(SampleWorld))

mysample =SampleWorld()

print(type(mysample))



class Dog():

    #__init__ refers to constructor for a class
    #we can pass any other keyword name instead of "self" but by convention we use "self"
    def __init__(self,breed,name,spots):

       #to take attribute ,we take in the argument
       #assign it using "self.attribute_name"

        #self.breed =mybreed
        self.breed = breed
        self.name = name
        self.spots = spots

#Dog(mybreed ='lab')
my_dog=Dog(breed='Lab', name='Tomy', spots=True)

print(type(my_dog))



print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)