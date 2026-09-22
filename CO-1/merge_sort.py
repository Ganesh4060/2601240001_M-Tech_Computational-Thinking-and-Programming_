def merge_sort(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2

    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        # Sort based on MARKS
        if left[i][1] >= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


# Input
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students.append([name, marks])


# Sort based on marks
students = merge_sort(students)

print("\nStudents sorted by marks:")
for student in students:
    print(student[0], "-", student[1])


# Scholarship students
print("\nScholarship Students:")

for student in students:
    if student[1] >= 90:
        print(student[0], "-", student[1])


# Search student
search = input("\nEnter student name to search: ")

for student in students:
    if student[0].lower() == search.lower():
        print("Student Found")
        print("Name:", student[0])
        print("Marks:", student[1])
        break
else:
    print("Student not found")
