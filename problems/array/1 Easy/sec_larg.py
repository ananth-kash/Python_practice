a=[2,33,221,3]
lar=sec_lar=a[0]
for i in a:
    if i>lar:
        sec_lar=lar
        lar=i
print(sec_lar)