s = open('24 (5).txt').readline()
s = s.replace('A1','0').replace('A2','0').replace('B2','0').replace('B1','0')
for i in range(1,1000):
    if ('0'*i) in s:
        print(i)
