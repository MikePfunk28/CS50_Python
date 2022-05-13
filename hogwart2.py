students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
# [] means list {} means dictionary - collection of key/value pairs
# creating multiple dictionaries, with KEYS and VALUES, word and meaning. {dict} - [{dict}, {dict}]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")