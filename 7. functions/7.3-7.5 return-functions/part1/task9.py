# Найти всех

def find_all(target: str, symbol: str) -> list:
    res = []
    for i in range(len(target)):
        if target.find(symbol, i) not in res and target.find(symbol, i) != -1:
           res.append(target.find(symbol, i))
    return res

print(find_all('abcdabcaaa', 'a'))
print(find_all('abcadbcaaa', 'e'))
print(find_all('abcadbcaaa', 'd'))