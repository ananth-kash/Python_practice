a=[2,4,10,20]
print(max(a))
max_var=a[0]
for i in a:
    if  i>max_var:
        max_var=i
print(max_var)