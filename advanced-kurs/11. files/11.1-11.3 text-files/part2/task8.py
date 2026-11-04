# Необычные страны

with open(input(), "r", encoding="utf-8") as file:
    data = [line.split() for line in file.readlines() if line.split()[0].startswith("G")]
    print(*[info[0] for info in data if int("".join(i for i in info[1] if i.isdigit())) > 500_000], sep="\n")
