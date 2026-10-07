# Сбой в системе

org_text = input()

start = org_text.find("[")
result = ""

decode = org_text[start:].rstrip("!?").replace("[", " ").replace("]", "").replace("u", "").replace("-", "")

for c in decode:
    if c.isdigit():
        if len(result) != 4:
            result += c
        if len(result) == 4:
            org_text = org_text.replace(f"[u-{result}]", chr(int(result)))
            result = ""

print(org_text)



