b=[20,12.34,32,4,55]
c=[20,30,44,55,65,66]
def issort(a):
    sorted=True
    for i in range(len(a)-1):
        if((a[i+1])<(a[i])):
            sorted=False
            break
    print(sorted)

issort(b)
issort(c)