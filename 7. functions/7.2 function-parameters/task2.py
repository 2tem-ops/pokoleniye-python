# Посчитай регистры

def print_case_counts(s: str):
    uppercase = 0
    lowercase = 0
    for i in s:
        if not i.isalpha():
            continue
        elif 1040 <= ord(i) <= 1071:
            uppercase += 1
        elif 1072 <= ord(i) <= 1103:
            lowercase += 1
        elif 97 <= ord(i) <= 122:
            lowercase += 1
        elif 65 <= ord(i) <= 90:
            uppercase += 1

    print(f"Букв в верхнем регистре: {uppercase}",
          f"Букв в нижнем регистре: {lowercase}",
          sep="\n")

print_case_counts("fd-7lg-td0_vF54Kds-fgmd+aEJ/NF#5hvq!4x")