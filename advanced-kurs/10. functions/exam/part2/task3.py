words = ['пионы', 'тюльпаны', 'розы']

print(*[i for i in (map(lambda x: '"' + x + '"', words))], sep=" ")