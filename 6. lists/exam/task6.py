# Валидный номер

phone = input()
s = phone.split("-")

flag1 = False
flag2 = False

if len(s) == 4:
    for i in range(1, len(s) - 1):
        if len(s[0]) == 1 and s[0] == "7" and len(s[-1]) == 4:
               if len(s[i]) == 3:
                   flag1 = True

    if phone.count("-") == 3 and len(phone) == 14 and phone.replace("-", "").isdigit():
        flag2 = True

elif len(s) == 3:
    for i in range(len(s) - 1):
        if len(s[-1]) == 4:
            if len(s[i]) == 3:
                flag1 = True

    if phone.count("-") == 2 and len(phone) == 12 and phone.replace("-", "").isdigit():
        flag2 = True

if flag1 and flag2:
    print("YES")
else:
    print("NO")