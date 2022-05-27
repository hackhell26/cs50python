# A list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otther"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherine", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")