s = open('24 (8).txt').readline()
s = s.replace('CA','0')
for i in range(1,1000):
    if '0'*i in s:
        print(i)
