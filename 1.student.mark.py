students = []
courses = []
marks = []
sn = 0
cn = 0


def input_stu_no():
    return int(input("Number of students? "))


def input_crs_no():
    return int(input("Number of courses? "))


def input_stu_info():
    for i in range(sn):
        print(f"Student number {i+1}")
        students.append([input("Student ID? "), input("Student name? "), input("Student DoB? ")])


def input_crs_info():
    for i in range(cn):
        print(f"Course number {i+1}")
        courses.append([input("Course ID? "), input("Course name? ")])


def input_marks():
    crs_id = input("Course ID to input marks? ")
    for crs in courses:
        if crs[0] == crs_id:
            for stu in students:
                mark = float(input(f"Input mark for {stu[1]}: "))
                marks.append([crs_id, stu[0], mark])


def list_crs():
    print("Courses: ")
    print(courses)


def list_stu():
    print("Students: ")
    print(students)


def show_marks():
    crs_id = input("Course ID to show marks? ")
    for m in marks:
        if m[0] == crs_id:
            for stu in students:
                if stu[0] == m[1]:
                    print(f"{stu[1]}: {m[2]}")


if __name__ == '__main__':
    sn = input_stu_no()
    input_stu_info()
    cn = input_crs_no()
    input_crs_info()
    list_stu()
    list_crs()
    input_marks()
    show_marks()

