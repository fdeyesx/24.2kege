s = open('24 (3).txt').readline()
s = s.replace('KOT','0')
for i in range(1,1000):
    if ('0'*i) in s:
        print(i)
