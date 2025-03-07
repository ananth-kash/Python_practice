a=[12,44,664,33,22,333,22,12,5,12,12,3,4,5]
count=0
element=0
for i in a:
    if (count==0):
        element=i
        count+=1
    elif(i==element):
        count+=1
    elif(i!=element):
        count-=1
print([element,count])
    