letters = {4: 'К', 65: 'Щ', 12: 'П', 41: 'М', 36: 'У'}
remove_keys = [12, 65, 14, 37]

print({k: v for k, v in letters.items() if k not in remove_keys})