student_grades = {}
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n")

while True:
    command = input(menu_prompt).lower().strip()
    if command == '1':
        name, grade = input(grade_prompt).split()
        student_grades[name] = grade
    elif command == '2':
        student = input('Which student to delete?')
        del student_grades[student]
    elif command == '3':
        print(student_grades)
    elif command == '4':
        break
    else:
        print('Unrecognized command.')

