# Правильная скобочная последовательность

def is_correct_bracket(text: str) -> bool:
    while "()" in text:
        text = text.replace("()", "")
    return len(text) == 0


print(is_correct_bracket('()(()())'))
print(is_correct_bracket(')(())('))
