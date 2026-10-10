# Змеиный регистр

def convert_to_python_case(text: str) -> str:
    s = text[0]

    for i in range(len(text) - 1):
        if i != 0:
            s += text[i]
        if text[i + 1].isupper():
            s += "_"

    return s.lower() + text[-1]

print(convert_to_python_case('FBIIsWatchingYou'))
print(convert_to_python_case('IsPrimeNumber'))



