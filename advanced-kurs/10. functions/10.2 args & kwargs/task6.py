def info_kwargs(**kwargs) -> None:
    for k, v in sorted(kwargs.items()):
        print(f"{k}: {v}")

info_kwargs(city='Perm', name='Tony', height=175)