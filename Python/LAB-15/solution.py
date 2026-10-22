students = {
    "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]}
}

while True:
    print("\n===== STUDENT INFORMATION MANAGEMENT SYSTEM =====")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print("\n--- Enrolled Student Records ---")
        for roll, student in students.items():
            print("Roll No:", roll, "| Name:", student["Name"],
                  "| Branch:", student["Branch"],
                  "| Semester:", student["Semester"],
                  "| Marks:", student["Marks"])
        print("Total Enrolled Students:", len(students))

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")

        student = students.get(roll)

        if student:
            print("\nName:", student["Name"])
            print("Branch:", student["Branch"])
            print("Semester:", student["Semester"])
            print("Marks:", student["Marks"])
        else:
            print("Student record not found.")

    elif choice == "3":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Roll Number already exists.")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch: ")
            semester = input("Enter Semester: ")

            marks = []
            for i in range(3):
                mark = int(input("Enter marks for Subject " + str(i + 1) + ": "))
                marks.append(mark)

            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Marks": marks
            }

            print("Student registered successfully.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")

        if roll in students:
            print("1. Update Branch")
            print("2. Update Semester")

            field = input("Choose field to update: ")

            if field == "1":
                students[roll]["Branch"] = input("Enter new Branch: ")
                print("Branch updated successfully.")

            elif field == "2":
                students[roll]["Semester"] = input("Enter new Semester: ")
                print("Semester updated successfully.")

            else:
                print("Invalid choice.")

        else:
            print("Student record not found.")

    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ")

        if roll in students:
            student = students[roll]
            marks = student["Marks"]

            total = sum(marks)
            average = total / len(marks)

            if average >= 40:
                result = "PASS"
            else:
                result = "FAIL"

            print("\n===== ACADEMIC REPORT =====")
            print("Student Name:", student["Name"])
            print("Roll Number:", roll)
            print("Subject Marks:", marks)
            print("Total Marks:", total, "/", len(marks) * 100)
            print("Average Marks:", round(average, 2), "%")
            print("Final Result:", result)

        else:
            print("Student record not found.")

    elif choice == "6":
        roll = input("Enter Roll Number to delete: ")

        student = students.pop(roll, None)

        if student:
            print("Student", student["Name"], "deleted successfully.")
        else:
            print("Student record not found.")

    elif choice == "7":
        print("Thank you for using Student Information System.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 7.")