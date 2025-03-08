
def pascal(levels: int):
    result=[]
    for i in range(0,levels):
        row = [None]*(i+1)
        row[0], row[-1]=1,1
        for j in range(1,len(row)-1):
            row[j]=result[i-1][j-1]+result[i-1][j]
        result.append(row)
    return result




a=4
print(pascal(a))






