s = open('24 (2).txt').readline()
#s = 'ADGCBAGDTYRJNKFLSRBFCNDSUFJMALDFJFUS'
p = ''
mxp = ''
for j in s:
    p += j
    if p.count('D') < 3:
        if len(p) > len(mxp):
            mxp = p
    else:
        p = ''
print(len(mxp))
