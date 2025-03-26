s = open('24 (13).txt').readline()
#s = 'ZYXYXYZXYXYXYYZXYZYXXY'
p = ''
mxp = ''
for i in s:
    p += i
    if p.count('Z') == 0:
        if 'XX' not in p or 'YY' not in p:
            if len(p) > len(mxp):
                mxp = p
    else:
        p = p[p.find('Z')+1:]
print(len(mxp))
