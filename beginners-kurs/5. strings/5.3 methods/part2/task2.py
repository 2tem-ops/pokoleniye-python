# Минута генетики

s = input().lower()
a, g, c, t = 0, 0, 0, 0

a += s.count("а")
g += s.count("г")
c += s.count("ц")
t += s.count("т")

print(
    f"Аденин: {a}",
    f"Гуанин: {g}",
    f"Цитозин: {c}",
    f"Тимин: {t}",
    sep="\n"
)