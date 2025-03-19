s = open('24 (6).txt').readline()
#s = 'ARHDNGHAFNBFNAKDMFGHJAR'
p = ''
mxp = ''
for i in s:
    p += i
    if p.count('R') == 0:
        if p.count('A') < 4:
            if len(p) > len(mxp):
                mxp = p
    else:
        p = ''
print(len(mxp))
