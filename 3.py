s = open('24 (2).txt').readline()
#s = 'XXXXYYZXYZYXZXXXXYYZ'
k = 0
for i in range(0,len(s)-4):
    if s[i]+s[i+1]+s[i+2]+s[i+3] == 'XXXX':
        k+=1
print(k)

