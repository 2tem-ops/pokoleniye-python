students = {'Сергей': (165, 62), 'Дима': (178, 61), 'Катя': (162, 62), 'Диана': (168, 69)}

print({k: v for k, v in students.items() if v[0] > 167 and v[1] < 75})