student_name = "Sanil"
marks = {"james": 90, "Jules":55, "Arthur": 77}

for student in marks:
    if student ==student_name:
        print(marks[student])
        break
else:
    print("No Entry with that name found.")

