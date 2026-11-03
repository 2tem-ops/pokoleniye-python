words = ['justice', 'orange', 'plant', 'sunday']

print(*sorted(filter(lambda w: len(w) == 6, words)))