s = open('24 (22).txt').readline()
s = s.replace('()','++',9999)
print(s.find('()')+1)
