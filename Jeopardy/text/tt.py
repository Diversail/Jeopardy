f = open('test', 'r+')
fl=f.readlines()
lines = [lines for lines in f.readlines()]
lines = fl.strip()
f.close()
print(fl-'\n')
print(lines)
