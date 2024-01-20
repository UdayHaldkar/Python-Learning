# normal function Expression
# def sqr(num):
#   return num**2


#lambda expression
# lambda function is also known as anonymous function because its only use onces

## no "def" keyword no function name
sqr = lambda num:num**2

print(sqr(3))


#or
mynums=[1,4,8,2,3,5,3,]
print(list(map(lambda num:num*2,mynums)))

#by filter
print(list(filter(lambda num:num %2==0,mynums)))
