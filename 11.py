from re import *
s = open('24 (10).txt').readline()
for j in 'ABC':
    for i in 'ABC':
        s = s.replace(f'{j}{i}','0')
a = r'[0]+'
k = [len(x) for x in findall(a,s)]
print(max(k))
