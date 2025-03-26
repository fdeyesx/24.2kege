from re import *
s = open('24 (23).txt').readline()
a = r'[A-Z]+'
k = [len(x) for x in findall(a,s)]
print(max(k))
