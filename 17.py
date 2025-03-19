s = open('24 (7).txt').readline()
#s = 'CCBAABABCBC'
p = ''
mxp = 0
o = set()
for i in range(0, len(s) - 2):
    if s[i] == s[i+2]:
        l = s[i:i+3]
        p1 = list(l)
        p1[-1], p1[-3] = '+', '+'
        for a in p1:
            p = a + p
        p1 = []
for j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    k = p.count(j)
    if mxp == 0:
        mxp = k
        o.add(j)
    if k > mxp:
        mxp = k
        o = set()
        o.add(j)
    if k == mxp:
        o.add(j)
o = list(o)
print(o[0],mxp)
