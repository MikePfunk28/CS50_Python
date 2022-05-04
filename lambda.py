people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"}
]

#def f(person):
#    return person["name"]
# (can replace above fuction with lambda)

people.sort(key=lambda person: person["name"])

print(people)

