from immigrant import Student, Doctor, Teacher
from ward import Ward

# Create instances
student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")

# Test describe method for each instance
print(student1.describe())  # Expected: Student - Name: studentA - YoB: 2010 - Grade: 7
print(teacher1.describe())  # Expected: Teacher - Name: teacherA - YoB: 1969 - Subject: Math
print(doctor1.describe())   # Expected: Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists

# Create a ward and add people
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(Doctor(name="doctorB", yob=1975, specialist="Cardiologists"))
ward1.add_person(Teacher(name="teacherB", yob=1995, subject="History"))

# Describe the ward
print(ward1.describe())

# Count doctors
print(f"Number of doctors: {ward1.count_doctor()}")  # Expected: 2

# Sort people by age (yob)
ward1.sort_age()
print("After sorting by age:")
print(ward1.describe())

# Compute average year of birth for teachers
print(f"Average year of birth (teachers): {ward1.compute_average()}")  # Expected: Average year of birth for teachers

