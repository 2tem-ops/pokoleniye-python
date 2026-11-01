# Код Морзе

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
morse = dict(zip(letters, codes))

s = [i for i in input().upper() if i.isalnum()]
print(" ".join(morse[letter] for letter in s))