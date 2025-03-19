s = open('24 (4).txt').readline()
s = 'AFCDOFAOFCFAFCFADCOFADOAFC'
p = ''
mxp = ''
for i in s:
    p += i
    p1 = p
    for k in 'AO':
        p1 = p1.replace(k,'+')
    for l in 'CDF':
        p1 = p1.replace(k, '-')
    if '-++-' not in p:
        if len(p) > len(mxp):
            mxp = p
    else:
        p = p[-3:]
print(len(mxp))
 
