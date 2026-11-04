# Сумма чисел в файле

with open(input(), "r", encoding="utf-8") as file:
    process = file.read()
    for i in process:
        if i not in "1234567890":
            process = process.replace(i, " ")
    print(sum(int(i) for i in process.split()))