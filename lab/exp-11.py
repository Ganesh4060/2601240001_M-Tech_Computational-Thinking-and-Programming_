def calculate_total(marks: list[float]) -> float:
    """Calculate the total marks."""
    return sum(marks)


def calculate_average(marks: list[float]) -> float:
    """Calculate the average marks."""
    if not marks:
        raise ValueError("Marks list cannot be empty")

    return calculate_total(marks) / len(marks)


def calculate_grade(average: float) -> str:
    """Calculate grade based on average marks."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def validate_marks(marks: list[float]) -> None:
    """Validate that all marks are between 0 and 100."""
    for mark in marks:
        if mark < 0 or mark > 100:
            raise ValueError(
                "Marks must be between 0 and 100"
            )


def generate_result(
    name: str,
    marks: list[float]
) -> dict[str, object]:
    """Generate the complete student result."""

    validate_marks(marks)

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    return {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }


def main() -> None:
    """Main application."""

    print("===== STUDENT GRADE CALCULATOR =====")

    name = input("Enter student name: ")

    marks = []

    for i in range(3):
        mark = float(
            input(f"Enter marks for subject {i + 1}: ")
        )
        marks.append(mark)

    try:
        result = generate_result(name, marks)

        print("\n===== STUDENT RESULT =====")
        print("Name    :", result["name"])
        print("Marks   :", result["marks"])
        print("Total   :", result["total"])
        print("Average :", round(float(result["average"]), 2))
        print("Grade   :", result["grade"])

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()