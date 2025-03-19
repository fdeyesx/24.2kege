s = open('24 (7).txt').readline()
#s = 'ARHDNGHAFNBFNAKDMFGHJAR'
p = set()
mxp = []
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    k = s.count(i)
    if len(mxp) == 0:
        mxp.append(k)
        p.add(i)
    if k > max(mxp):
        mxp = []
        p = set()
        mxp.append(k)
        p.add(i)
    if k == max(mxp):
        p.add(i)
print(p)
