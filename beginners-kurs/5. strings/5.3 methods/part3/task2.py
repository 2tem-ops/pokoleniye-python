# Проверь никнейм

nickname = input()
n = nickname[1:]

flag = False

if nickname[0] == "@" and n.isalnum():
    if n.isdigit():
        if 5 <= len(nickname) <= 15:
            flag = True
    else:
        if n.islower() and 5 <= len(nickname) <= 15:
            flag = True

if flag:
    print("Correct")
else:
    print("Incorrect")


