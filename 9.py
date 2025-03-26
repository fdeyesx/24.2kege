from re import *
s = open('24 (8).txt').readline()
a = r'([CA]+)+C?'
k = [len(x) for x in findall(a,s)]
print(max(k))
