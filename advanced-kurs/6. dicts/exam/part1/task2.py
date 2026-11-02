emails = {
    'gmail.com': ['johnny', 'monkey-man'],
    'hotmail.com': ['chani'],
    'yandex.ru': ['petrpn', 'rtgxv5dsfsd4'],
}

res = []

for k, v in emails.items():
    for i in range(len(v)):
        res.append(f"{v[i]}@{k}")

print(*[i for i in sorted(res)], sep="\n")