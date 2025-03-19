s = open('24 (9).txt').readline()
#s = '12345678912333445566778899'
p = ''
mxp = ''
for j in s:
    p += j
    if len(p) > 2:
        if int(p[-2]) < int(p[-1]) or int(p[-2]) == int(p[-1]):
            if len(p) > len(mxp):
                mxp = p
                print(p)
        else:
            p = p[-1:]
    else:
        p = p
print(len(mxp))
