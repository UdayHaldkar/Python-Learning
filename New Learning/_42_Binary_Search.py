pos =-1

def search(lst,n):
    l=0
    u=len(lst)-1

    while l <=u:
        mid = (l+u)//2

        if lst(mid) == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid]<n:
                l=mid+1
            else:
                u=mid-1


lst =[23,43,1,6,5,90,3,9]
n=90

if search(lst,n):
    print("Found at ",pos)
else:
    print("Not Found")