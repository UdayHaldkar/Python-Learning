print("This is a string {}".format("inserted"))

print("The {} {} {}".format("fox","brown","quick"))
print("The {1} {0} {2}".format("fox","brown","quick"))
print("The {b} {q} {f}".format(f="fox",b= "brown",q ="quick"))


#float formatting

result =100/77
print(result)

#printing precise value
print("the result was {r:1.2f}".format(r=result))

#Fstring

name ="jose"

print(f"hello, his name is {name}")
