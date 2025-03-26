s = open('24 (12).txt').readline()
#s = 'AFCDOFAOFCFAFCFADCOFADOAFC'
p = ''
mxp = ''
for k in 'AO':
    s = s.replace(k, '+')
for l in 'CDF':
    s = s.replace(l, '-')
for i in s:
    p += i
    p1 = p
    if '-++-' not in p:
        if len(p) > len(mxp):
            mxp = p
    else:
        p = p[-3:]
print(len(mxp))
