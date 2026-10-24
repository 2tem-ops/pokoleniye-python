# Палиндром

word = input()

palindrome = False

if word[::-1] == word:
    palindrome = True

if palindrome:
    print("YES")
else:
    print("NO")