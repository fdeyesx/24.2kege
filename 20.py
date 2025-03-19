s = open('24 (10).txt').readline()
#s = 'adhfndfkeusndhfad'
p = ''
mxp = ''
for j in s:
    p += j
    if 'ad' not in p and 'da' not in p:
        if len(p) > len(mxp):
            mxp = p
    else:
        p = p[-1]
print(len(mxp))
