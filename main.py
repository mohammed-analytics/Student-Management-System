from student import *
from leave import *

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        addstudent()

    elif choice == 2:
        viewstudent()

    elif choice == 3:
        searchstudent()

    elif choice == 4:
        deletestudent()

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice")


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")

    print("\n--- Leave Management ---")
    print("5. Apply Leave")
    print("6. View Leave")
    print("7. Approve Leave")
    print("8. Reject Leave")

    print("\n9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        addstudent()

    elif choice == 2:
        viewstudent()

    elif choice == 3:
        searchstudent()

    elif choice == 4:
        deletestudent()

    elif choice == 5:
        applyleave()

    elif choice == 6:
        viewleave()

    elif choice == 7:
        approveleave()

    elif choice == 8:
        rejectleave()

    elif choice == 9:
        print("Thank you!")
        break

    else:
        print("Invalid choice")

