s = open('24 (6).txt').readline()
s = s.replace('NPO','0').replace('PNO','1')
k = []
for i in range(1,1000):
    if ('0'*i) in s:
        k.append(i)
for i in range(1,1000):
    if ('1'*i) in s:
        k.append(i)
for i in range(1,1000):
    for j in range(1,1000):
        if ('0'*j+'1' * i) in s:
            k.append(i)
print(max(k))
