# Папка в папке

def is_subfolder(folder_dict: dict, subfolder: str, folder: str) -> bool:
    for k, v in folder_dict.items():
        if subfolder in v:
            if k == folder:
                return True
            else:
                return is_subfolder(folder_dict, k, folder)
    return False


folder_system = {
    'K': ['A', 'B', 'K8', 'K9'],
    'B': ['B1', 'B2', 'B4'],
    'A': ['A7', 'A8', 'A9', 'P', 'R'],
    'P': ['Y', 'P18', 'P21', 'X'],
    'Y': ['U', 'W'],
}
print(is_subfolder(
    folder_system, 'P18', 'B',
))
print(is_subfolder(
    folder_system, 'W', 'X',
))
print(is_subfolder(
    folder_system, 'X', 'K',
))