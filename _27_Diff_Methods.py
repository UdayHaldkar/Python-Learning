# 3 - types of methods
# class method, intance method(_init_), Static method

class student():
    school ="kv"  #static or class variable

#intance method
    def __init__(self,m1,m2,m3):
        self.m1=m1   #intance variable
        self.m2=m2
        self.m3=m3


    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    ##class method
    @classmethod  #decorator
    def info(cls):
        return cls.school

# static method is a type of method which have nothing to with intance or class variable
    @staticmethod
    def details():
        print("This is a Static variable")



s1 =student(23,34,23)
s2 =student(76,45,12)

print(s1.avg())
print(s2.avg())

print(student.info())

student.details()