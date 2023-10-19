students = []

student1_info = {
    "first_name": "sol",
    "last_name": "hyun",
    "student_no": 3498
}

student2_info = {
    "first_name": "suzy",
    "last_name": "bae",
    "student_no": 1345
}

student3_info = {
    "first_name": "cola",
    "last_name": "hyun",
    "student_no": 4593
}

student4_info = {
    "first_name": "coca",
    "last_name": "hyun",
    "student_no": 9348
}

students.append(student1_info)
students.append(student2_info)
students.append(student3_info)
students.append(student4_info)

# print(students)

# def sort_help(d):
#     return d["student_no"]

sorted_students = sorted(students, key=lambda x: x["student_no"])
print(sorted_students)
