stud_list = ['Pitok', 'Kulas', 'ADS', 'JJ', 'sample1', 'sample2']
course_list = ['BSIT', 'CRIM', 'CRIM', 'BSIT', 'BSEE', 'BSEE']

def add_student():
    student = input("Enter student name: ")
    course = input("Enter student course: ")
    stud_list.append(student)
    course_list.append(course)
    print("DONE ADDED")

def display_all_students():
    for i in range(len(stud_list)):
        print(stud_list[i],"=", course_list[i])

def display_students_per_course():
    course_name = input("Enter the course name to display students: ")
    students = [stud_list[i] for i in range(len(stud_list)) if course_list[i] == course_name]
    if students:
        print("Students in " + course_name + ":")
        for student in students:
            print(student)
    else:
        print("No students found for course: " + course_name)

while True:
    print("\n================================")
    print("1 = add student")
    print("2 = display all students")
    print("3 = display student per course")
    print("4 = EXIT PROGRAM")
    i = int(input("\nEnter your number: "))
    print("")

    if i == 1:
        add_student()
    elif i == 2:
        display_all_students()
    elif i == 3:
        display_students_per_course()
    elif i == 4:
        break
print("DONE END!")