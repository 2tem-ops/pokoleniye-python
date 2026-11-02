# Опасный вирус

admin = {}

for _ in range(int(input())):
    file = input().split()
    permissions = ["write" if i == "W" else "execute" if i == "X" else "read" for i in file[1:]]

    admin[file[0]] = permissions

for _ in range(int(input())):
    operation, file = input().split()
    if operation in admin[file]:
        print("OK")
    else:
        print("Access denied")

