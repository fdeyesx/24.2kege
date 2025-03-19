s = open('24 (7).txt').readline()
s = 'CCBAABABCBC'
p = ''
mxp = 0
p1 = ''
o = set()
for i in s:
    p += i
    if len(p) == 3:
        if p[0] == p[-1]:
            p1 += p[1]
    else:
        p = ''
for j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    k = p1.count(j)
    if k > mxp:
        mxp = k
        o.add(j)
    if k == mxp:
        o.add(j)
o = list(o)
print(o[-1],mx
