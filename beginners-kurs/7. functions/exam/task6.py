# Магические даты

def is_magic(date: str) -> bool:
    date = [int(i) for i in date.split(".")]
    return date[0] * date[1] == date[-1] % 100

print(is_magic('03.11.2032'))
print(is_magic('15.12.1234'))
print(is_magic('10.09.1990'))