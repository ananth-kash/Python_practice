a=[12,13,14,14,15]
b=[]
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        b.append(i+1)
for j in b:
    a.remove(a[j])
print(a)
# o(n^2) time and o(n) space
a=list(set(a))
print(a)
# o(n) time and o(n) space
