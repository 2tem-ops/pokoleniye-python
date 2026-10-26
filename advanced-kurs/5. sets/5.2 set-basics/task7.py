# Все 10 цифр

s1, s2 = input(), input()
print("YES" if len(set(s1 + s2)) == 10 else "NO")