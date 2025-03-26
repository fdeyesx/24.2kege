s = open('24 (7).txt').readline()
s = s.replace('ABA','0').replace('ACA','0').replace('AAA','0')
s = s.replace('CCC','A').replace('CAC','1').replace('CBC','1')
k = []
for i in range(1,1000):
    if ('0'*i) in s:
        k.append(i)
print('--')
for i in range(1,1000):
    if ('1'*i) in s:
        k.append(i)
print('--')
print(max(k))
