d = {}                        # Empty dictionary
d = {'a': 1, 'b': 2, 'c': 3, 'c':4}  # Initialized dictionary
value = d['c']
print(d)
print(value)
print('c' in d)
del d['c']
print(d)
print(d.pop('b'))
d['d']=2
print(d)
print(4 in d.values())
print(list[d.keys()])
print(list[d.values()])
print(list[d.items()])
from collections import Counter
count_dict = Counter(['a', 'b', 'a', 'c', 'b', 'a'])  # Counter({'a': 3, 'b': 2, 'c': 1})
print(count_dict)
from collections import defaultdict
d = defaultdict(list)          # Default value is an empty list for missing keys
d['a'].append(1)               # d = {'a': [1]}
