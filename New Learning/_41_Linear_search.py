pos =-1
def search(lst,n):
    i=0
    while i < len(lst):
        if lst[i] == n:
            globals()['pos']=i
            return True
        i =i+1

    return False
lst =[1,4,2,5,33,6,9]
#n =input("Enter the Number ")
n=6

if search(lst,n):
    print("Found at ",pos)
else:
    print("Not Found")