name = ["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "  ]

def clean(names):
    return [name.strip().title() for name in names]

print(clean(name))