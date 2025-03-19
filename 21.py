s = open('24 (11).txt').readline()
p = ''
for j in s:
    p += j
    if p.count('f') == '123':
        print(len(p))
        break
