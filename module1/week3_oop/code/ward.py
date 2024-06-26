# Import classes from immigrant.py
from immigrant import Student, Doctor, Teacher

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        descriptions = [person.describe() for person in self.people]
        return f"Ward Name: {self.name}\n" + "\n".join(descriptions)

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob, reverse=True)

    def compute_average(self):
        teacher_yobs = [person.yob for person in self.people if isinstance(person, Teacher)]
        if teacher_yobs:
            return sum(teacher_yobs) / len(teacher_yobs)
        return 0
