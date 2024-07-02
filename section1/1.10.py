student_details = {}
N = int(input("Enter the number of students: "))
for i in range(N):
    name = input(f"Enter the name of student {i+1}: ")
    roll_no = int(input(f"Enter the roll number of student {i+1}: "))
    total_mark = float(input(f"Enter the total mark of student {i+1}: "))
    student_details[roll_no] = {"name": name, "total_mark": total_mark}

highest_mark = max(student_details, key=lambda x: student_details[x]["total_mark"])

print(f"Student with the highest total mark: ")
print(f"Roll Number: {highest_mark}")
print(f"Name: {student_details[highest_mark]['name']}")
print(f"Total Mark: {student_details[highest_mark]['total_mark']}")
