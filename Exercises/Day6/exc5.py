countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

for content in zip(countries):
    file = open(f"{content}.txt", "w")
    file.write(f"{content}")
    file.close()
