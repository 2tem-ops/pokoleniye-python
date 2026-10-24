# Посчитай количества

def print_symbol_counts(s: str):
    lst = [str(s.lower().count(i)) + i for i in sorted(s.lower())]
    ltr = [i[-1] for i in lst]
    res = []

    for i in ltr:
        if i not in res:
            res.append(i)

    count = [s.lower().count(i) for i in res]

    for i in range(len(res)):
        print(res[i], str(count[i]), sep=": ")

print_symbol_counts("Каспийск")