import json
def addstudent():
    file=open("student.json","r")
    students=json.load(file)
    file.close()
    studentid=int(input("enter your id"))
    name=(input("enter your name"))
    course=input("enter the course")
    student={
        "id":studentid,
        "name":name,
        "course":course
    }
    students.append(student)
    file=open("student.json","w")
    json.dump(students,file,indent=4)
    file.close()
    print("successfully added")
addstudent()

def viewstudent():
    file=open("student.json","r")
    students=json.load(file)
    file.close()
    for student in students:
        print("id:",student["id"])
        print("name:",student["name"])
        print("course:",student["course"])
        print()
viewstudent()
import json
def searchstudent():
    file=open("student.json","r")
    students=json.load(file)
    file.close()
    studentid=int(input("enter your id"))
    for student in students:
        if student["id"]==studentid:
            print("id:",student["id"])
            print("name:",student["name"])
            print("course:",student["course"])
            print()


def deletestudent():

    file = open("student.json", "r")
    students = json.load(file)
    file.close()

    studentid = int(input("Enter your id: "))

    found = False

    for student in students:

        if student["id"] == studentid:

            students.remove(student)
            found = True
            break

    if found:

        file = open("student.json", "w")
        json.dump(students, file, indent=4)
        file.close()

        print("Student successfully deleted")

    else:
        print("Student ID not found")
deletestudent()




   
    

