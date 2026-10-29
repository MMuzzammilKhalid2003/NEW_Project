# grade_book.py
# A simple command-line grade book.
students = {}  # name -> list of marks
def show_menu():
    print("\n=== Grade Book ===")
    print("1. Add student")
    print("2. Show grades")
    print("0. Exit")
def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "0":
            print("Goodbye!")
            break  
        elif choice == "1":
            add_student()
        elif choice == "2":
            show_grades()
        else:
            print("Invalid option.")

def calculate_grade(average):
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 55:
        return "C"
    elif average >= 40:
        return "D"
    return "F"

def show_grades():
    if not students:
        print("No students yet.")
        return
    for name, marks in students.items():
        average = sum(marks) / len(marks)
        print(f"{name}: average {average:.1f}, grade {calculate_grade(average)}")
        break 

def add_student():
    name = input("Student name: ")
    marks = input("Marks separated by spaces: ")
    try:
      students[name] = [int(m) for m in marks.split()]
    except ValueError:
      print("Invalid input! Marks must be numbers.")


if __name__ == "__main__":
    main()              