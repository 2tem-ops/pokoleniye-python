# Инициалы

full_name = input()

lst = full_name.split()
initials = [lst[0][0], lst[1][0], lst[2][0], " "]

print(".".join(initials))