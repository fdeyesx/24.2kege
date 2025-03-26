s = open('24 (4).txt').readline()
s = s.replace('BA','0').replace('BO','0').replace('CA','0').replace('CO','0').replace('DA','0').replace('DO','0')
for i in range(1,1000):
    if ('0'*i) in s:
        print(i)
