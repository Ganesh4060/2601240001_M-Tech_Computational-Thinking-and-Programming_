class AttendanceSystem:

    def __init__(self):

        # Store student information
        self.students = []

        # Minimum required attendance
        self.minimum_attendance = 75

    # ------------------------------------------
    # 1. Add Student
    # ------------------------------------------

    def add_student(self):

        print("\n========== ADD STUDENT ==========")

        name = input("Enter student name: ")

        try:

            total_classes = int(
                input("Enter total classes conducted: ")
            )

            attended_classes = int(
                input("Enter classes attended: ")
            )

        except ValueError:

            print("Please enter numbers only.")
            return

        # Check values
        if total_classes <= 0:

            print("Total classes must be greater than 0.")
            return

        if attended_classes < 0:

            print("Attended classes cannot be negative.")
            return

        if attended_classes > total_classes:

            print(
                "Attended classes cannot be greater than "
                "total classes."
            )

            return

        # Calculate attendance
        percentage = (
            attended_classes / total_classes
        ) * 100

        # Store student
        student = {

            "name": name,
            "total": total_classes,
            "attended": attended_classes,
            "percentage": percentage
        }

        self.students.append(student)

        print("\nStudent added successfully.")

        print("Student Name :", name)

        print(
            "Attendance   :",
            round(percentage, 2),
            "%"
        )

    # ------------------------------------------
    # 2. Display All Students
    # ------------------------------------------

    def display_students(self):

        print("\n========== STUDENT ATTENDANCE ==========")

        if len(self.students) == 0:

            print("No students available.")

            return

        for student in self.students:

            print("--------------------------------------")

            print(
                "Student Name :",
                student["name"]
            )

            print(
                "Total Classes:",
                student["total"]
            )

            print(
                "Attended     :",
                student["attended"]
            )

            print(
                "Attendance   :",
                round(student["percentage"], 2),
                "%"
            )

            if student["percentage"] < 75:

                print("Status       : BELOW 75%")

            else:

                print("Status       : ELIGIBLE")

    # ------------------------------------------
    # 3. Find Students Below 75%
    # ------------------------------------------

    def below_75(self):

        print("\n========== STUDENTS BELOW 75% ==========")

        found = False

        for student in self.students:

            if student["percentage"] < 75:

                found = True

                print(
                    student["name"],
                    "-",
                    round(student["percentage"], 2),
                    "%"
                )

        if found == False:

            print(
                "No students have attendance below 75%."
            )

    # ------------------------------------------
    # 4. Find Top Attendance Student
    # ------------------------------------------

    def top_student(self):

        print("\n========== TOP ATTENDANCE ==========")

        if len(self.students) == 0:

            print("No students available.")

            return

        top = self.students[0]

        for student in self.students:

            if student["percentage"] > top["percentage"]:

                top = student

        print("Student Name :", top["name"])

        print(
            "Attendance   :",
            round(top["percentage"], 2),
            "%"
        )

    # ------------------------------------------
    # 5. Calculate Class Average
    # ------------------------------------------

    def class_average(self):

        print("\n========== CLASS AVERAGE ==========")

        if len(self.students) == 0:

            print("No students available.")

            return

        total_percentage = 0

        for student in self.students:

            total_percentage = (
                total_percentage +
                student["percentage"]
            )

        average = (
            total_percentage /
            len(self.students)
        )

        print(
            "Class Average Attendance :",
            round(average, 2),
            "%"
        )

    # ------------------------------------------
    # 6. Main Menu
    # ------------------------------------------

    def menu(self):

        while True:

            print("\n")
            print("==========================================")
            print("       STUDENT ATTENDANCE SYSTEM")
            print("==========================================")

            print("1. Add Student")
            print("2. Display All Students")
            print("3. Students Below 75%")
            print("4. Top Attendance Student")
            print("5. Class Average Attendance")
            print("6. Exit")

            print("==========================================")

            choice = input("Enter your choice: ")

            # Add student
            if choice == "1":

                self.add_student()

            # Display students
            elif choice == "2":

                self.display_students()

            # Below 75%
            elif choice == "3":

                self.below_75()

            # Top student
            elif choice == "4":

                self.top_student()

            # Class average
            elif choice == "5":

                self.class_average()

            # Exit
            elif choice == "6":

                print(
                    "\nThank you for using "
                    "Student Attendance System."
                )

                break

            else:

                print(
                    "Invalid choice. Please try again."
                )


# ==========================================
# START PROGRAM
# ==========================================

attendance = AttendanceSystem()

attendance.menu()