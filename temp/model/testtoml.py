import tomllib

with open('../../data/motivharia.toml', "rb") as f:
    data = tomllib.load(f)
    print(data)
    print(data['info']['title'])
    print(data['info']['description'])