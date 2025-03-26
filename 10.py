from re import *
s = open('24 (9).txt').readline()
a = r'(?:DBAC)+(?:DBA|DB|D)?'
k = [len(x) for x in findall(a,s)]
print(max(k))
