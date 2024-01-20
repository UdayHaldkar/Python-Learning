class computer():
    def __init__(self,cpu,ram):  #constructor
        self.cpu=cpu             #variable assignment
        self.ram=ram             #variable assignment

    def config(self):            #method
        print("The config is ",self.cpu,self.ram)

comp1 = computer("ryzen 3", "16gb")   #object declaration
comp2 =computer("i5","8gb")          #object declaration

comp1.config()                                  #object call (calling constructor of class)
comp2.config()