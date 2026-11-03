countries = ['Australia', 'Canada', 'Portugal', 'Japan']
capitals = ['Canberra', 'Ottawa', 'Lissabon', 'Tokyo']
population = [27_840_775, 41_575_585, 10_749_635, 122_950_000]

for country, capital, population in zip(countries, capitals, population):
    print(f"{capital} is the capital of {country}, population equal {population} people.")