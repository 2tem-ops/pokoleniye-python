# Текст -> словарь

def transform(text: str) -> dict:
    res = {}
    for index, char in enumerate(text):
        res.setdefault(char, set()).add(index)
    return res

print(transform('Аметист'))