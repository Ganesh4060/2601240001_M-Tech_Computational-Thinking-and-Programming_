from dataclasses import dataclass


# --------------------------------
# Traditional Class
# --------------------------------

class StudentTraditional:

    def __init__(
        self,
        student_id: int,
        name: str,
        department: str,
        marks: float
    ) -> None:
        self.student_id = student_id
        self.name = name
        self.department = department
        self.marks = marks

    def display(self) -> None:
        print(
            self.student_id,
            self.name,
            self.department,
            self.marks
        )


# --------------------------------
# Dataclass
# --------------------------------

@dataclass
class Student:

    student_id: int
    name: str
    department: str
    marks: float

    def display(self) -> None:
        print(
            self.student_id,
            self.name,
            self.department,
            self.marks
        )


# --------------------------------
# Objects
# --------------------------------

traditional_student = StudentTraditional(
    101,
    "Ganesh",
    "CSE",
    85.5
)

dataclass_student = Student(
    102,
    "Rahul",
    "CSE",
    90.0
)


print("Traditional Class:")
traditional_student.display()

print("\nDataclass:")
dataclass_student.display()

print("\nDataclass Representation:")
print(dataclass_student)