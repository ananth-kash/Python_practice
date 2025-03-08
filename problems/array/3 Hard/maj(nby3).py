a=[1,2,3,4,4,2,2,2,2,4,4]   
dct={}
for num in a:
    dct[num]=dct.get(num,0)+1
n=len(a)
threshold=n/3
result= [k for k, val in dct.items() if val>threshold]
print(result)

