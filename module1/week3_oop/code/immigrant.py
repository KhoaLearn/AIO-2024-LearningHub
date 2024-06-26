class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        return f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}"

class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        return f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}"

class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        return f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}"
