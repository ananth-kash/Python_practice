b=[7,1,5,3,6,4]
def find_maxprof(a):
    max_profit=0
    min_price=float('inf')
    for i in a:
        if i < min_price:
            min_price=i
        max_profit=max(max_profit,i-min_price)
    return max_profit

c=find_maxprof(b)
print(c)


