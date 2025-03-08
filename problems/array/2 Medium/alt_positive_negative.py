a=[10,20,40,-2,34,-4,-10,-2]

def alternate_nums(b):
    count_positve=0
    count_negative=1
    c=[0]*len(b)
    for i in b:
        if(i<0):
            c[count_negative]=i
            count_negative+=2
        else:
            c[count_positve]=i
            count_positve+=2
    return c

               
val=alternate_nums(a)
print(val)  