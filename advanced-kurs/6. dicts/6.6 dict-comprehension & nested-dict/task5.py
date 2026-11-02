s = '3:animal 4:house 8:tree 2:color 21:moon 31:fire 12:ship'


print(dict([[int(i) if i.isdigit() else i for i in i.split(":") ] for i in s.split()]))