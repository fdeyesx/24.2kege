from re import *
s = open('24 (11).txt').readline()
for j in '24':
    for i in '135':
        s = s.replace(f'{j}{i}','0')
a = r'[0]+'
k = [len(x) for x in findall(a,s)]
print(max(k))
