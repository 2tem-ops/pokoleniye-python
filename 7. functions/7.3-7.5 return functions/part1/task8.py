# Последнее вхождение

def get_last_index(data: list, value):
    if data.count(value) > 1:
        return len(data) - 1 - data[::-1].index(value)
    elif data.count(value) == 1:
        return data.index(value)
    else:
        return "ERROR!"

print(get_last_index(['⭐', '🟩', '🔵', '🔻', '🔶'], '🔺'))