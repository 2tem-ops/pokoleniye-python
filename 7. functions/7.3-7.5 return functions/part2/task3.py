# Ровно в одном

def is_one_away(word1: str, word2: str) -> bool:
    flag = False
    count = 0

    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1

    if count == 1:
        flag = True

    return flag

print(is_one_away('bike', 'hike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))