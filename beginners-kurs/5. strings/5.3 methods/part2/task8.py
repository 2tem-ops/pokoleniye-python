# Удаление фрагмента

text = input()
result = ""

first = text.find("h")
second = text.rfind("h")

print(text[:first] + text[second + 1:])