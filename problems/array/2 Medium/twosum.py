a=[2,7,9,100]
target=107
found = False
for i in range(len(a)):
    for j in range(i,len(a)):
        if(a[i]+a[j]==target):
            found=True
            print(i,j)       
if not found:
    print(0)
