## "self" is used to point toward the current object

class stu():
    def __init__(self):
        self.name="uday"
        self.age=22

    def update(self):
        b1.age=34

    def compare(self,b1):
        if self.age ==b1.age:
            return True
        else:
            return False

a1= stu()
b1= stu()

b1.name="Haldkar"

print(a1.name,a1.age)

print(b1.name,b1.age)

#update the value of age
b1.update()


#compare

if a1.compare(b1):
    print("They are same")
else:
    print("They are different")
