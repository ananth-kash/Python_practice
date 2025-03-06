lst = []                  # Empty list
lst = [10, 20, 30, 40, 50,"apple"]     # Initialized list
lst.append(100)             # O(1)
lst.insert(2, 500)          # O(n) - Expensive for large lists
lst.remove(40)             # O(n)
print(lst)
print(lst[0])
print(len(lst))
lst.pop(2)                # O(n) - If index is provided
lst.pop()
print(lst)
print(lst[0:3])#lst[start:end]            # O(k) where k = end - start
print(lst[4:1:-1])#lst[start:end:step]       # O(k)
print(lst.index('apple'))             # O(n) returns index where first occurence of x happens
lst.reverse()              # O(n)
print(lst)
lst.remove("apple")
new_lst = [x * 2 for x in lst if x > 2]  # O(n)
from functools import reduce
lst = list(map(lambda x: x * 2, lst))  # O(n)
lst = list(filter(lambda x: x > 2, lst)) # O(n)
print(lst)
total = reduce(lambda x, y: x + y, lst)  # O(n)
print(total)
lst1= list(range(1,15,2))               #lst = list(range(start, end, step))  # O(n)
print(lst1)
lst1= lst[1::]
shifted_nums= zip(lst,lst1)
shifted_Sums=list(map(lambda x:x[0]+x[1],shifted_nums))
print(shifted_Sums)
max(lst)
min(lst)
sum(lst)