# CSV-файл

from csv import DictReader

def read_csv(csv_file: str) -> list[dict]:
    with open(csv_file) as csv_file:
        reader = DictReader(csv_file)
        return list(reader)