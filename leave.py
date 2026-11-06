import json

def applyleave():

    file = open("student.json", "r")
    students = json.load(file)
    file.close()

    studentid = int(input("Enter student ID: "))

    found = False

    for student in students:
        if student["id"] == studentid:

            reason = input("Enter leave reason: ")
            date = input("Enter leave date: ")

            leave = {
                "student_id": studentid,
                "student_name": student["name"],
                "reason": reason,
                "date": date,
                "status": "Pending"
            }

            file = open("leave.json", "r")
            leaves = json.load(file)
            file.close()

            leaves.append(leave)

            file = open("leave.json", "w")
            json.dump(leaves, file, indent=4)
            file.close()

            print("Leave application submitted")
            found = True
            break

    if not found:
        print("Student ID not found")
applyleave()

def viewleave():

    file = open("leave.json", "r")
    leaves = json.load(file)
    file.close()

    if not leaves:
        print("No leave applications found")

    else:
        for leave in leaves:

            print("Student ID:", leave["student_id"])
            print("Student Name:", leave["student_name"])
            print("Reason:", leave["reason"])
            print("Date:", leave["date"])
            print("Status:", leave["status"])
            print("----------------------")
viewleave()

def approveleave():

    file = open("leave.json", "r")
    leaves = json.load(file)
    file.close()

    studentid = int(input("Enter student ID: "))

    found = False

    for leave in leaves:

        if leave["student_id"] == studentid:

            leave["status"] = "Approved"
            found = True

    if found:

        file = open("leave.json", "w")
        json.dump(leaves, file, indent=4)
        file.close()

        print("Leave successfully approved")

    else:
        print("Leave application not found")
approveleave

def rejectleave():

    file = open("leave.json", "r")
    leaves = json.load(file)
    file.close()

    studentid = int(input("Enter student ID: "))

    found = False

    for leave in leaves:

        if leave["student_id"] == studentid:

            leave["status"] = "Rejected"
            found = True

    if found:

        file = open("leave.json", "w")
        json.dump(leaves, file, indent=4)
        file.close()

        print("Leave successfully rejected")

    else:
        print("Leave application not found")
rejectleave()