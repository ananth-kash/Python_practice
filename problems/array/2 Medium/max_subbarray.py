a=[-3,-4,10,12,2,3,6,5,-20]
for i in a:
    current_sum=max_sum=a[0]
    for i in range(1,len(a)):
        current_sum=max(a[i],current_sum+a[i])
        
        max_sum=max(max_sum,current_sum)

print(max_sum)