# Oʍoглͷȹʜaя πoдʍeʜa

def replace_homoglyphs(text: str) -> str:
    homoglyphs = {
        'e': 'е', 'y': 'у', 'o': 'о', 'p': 'р', 'a': 'а',
        'ʍ': 'м', 'ʙ': 'в', 'Φ': 'Ф', 'k': 'к', 'x': 'х',
        'c': 'с', 'E': 'Е', 'T': 'Т', 'ȹ': 'ф', 'Ͷ': 'И',
        'ʜ': 'н', 'O': 'О', 'P': 'Р', 'A': 'А', 'H': 'Н',
        'K': 'К', 'Ƅ': 'ь', 'ͷ': 'и', 'ɯ': 'ш', 'X': 'Х',
        'C': 'С', 'B': 'В', 'M': 'М', 'π': 'п', '3': 'З',
        'Γ': 'Г', 'ʮ': 'ч',
    }

    return text.translate(str.maketrans(homoglyphs))

text = '''3дpaʙcтʙyйтe! Я ʍeʜeджep πo πoдбopy πepcoʜaлa ʙ Baзoʜ.
B cʙязͷ c ʜaлͷʮͷeʍ ʙakaʜcͷй ʍы πpͷглaɯaeʍ ʙac ʜa πoдpaбoтky ͷз дoʍa.
3apaбoтʜaя πлaтa бyдeт ʙыπлaʮeʜa ʙ тoт жe дeʜƄ – 3000-4000 pyб.
Чтoбы πpͷʜятƄ yʮacтͷe, cʙяжͷтecƄ c ʜaʍͷ ʮepeз Miligram: ... ͷлͷ 
πepeйдͷтe πo ykaзaʜʜoй ccылke: ...'''
print(replace_homoglyphs(text))

