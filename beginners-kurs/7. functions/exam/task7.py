# Панграммы

def is_pangram(text: str) -> bool:
    check = set(text.lower())
    if " " in check:
        check.remove(" ")
    return len(check) == 26

print(is_pangram("Jackdaws love my big sphinx of quartz"))
print(is_pangram("razy Fredrick bought many very exquisite opal"))
