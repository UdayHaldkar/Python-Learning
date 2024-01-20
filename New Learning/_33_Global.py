a =10

def glo():

    global a
    a=15
    print("Local ", a)

    globals()["a"] =20

glo()


print("Global ", a)