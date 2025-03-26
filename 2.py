s = open('24 (1).txt').readline()
#s = 'ADGCBAGDTYRJNKFLSRBFCNDSUFJMALDFJFUS'
p = ''
mxp = ''
for j in s:
    p += j
    if p.count('A') < 2:
        if len(p) > len(mxp):
            mxp = p
    else:
        p = p[p.find('D')+1:]
print(len(mxp))
