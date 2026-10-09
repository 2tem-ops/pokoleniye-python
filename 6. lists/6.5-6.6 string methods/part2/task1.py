# Количество артиклей

s = input().lower().split()
total = s.count("a") + s.count("an") + s.count("the")

print(f"Общее количество артиклей: {total}")
