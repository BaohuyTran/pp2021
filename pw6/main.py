import pickle

with open("students/students.text","r") as f1:
    students=f1.read()
    print(f"please enter the student info: \n{students}")
    pickledStudent=pickle.dumps(students)
    print(f"The information of pickled student is: \n{pickledStudent}")
with open("students/courses.text","r") as f2:
    courses=f2.read()
    print(f"please enter the course's info: \n{courses}")
    pickledCourse=pickle.dumps(courses)
    print(f"The information of pickled course is: \n{pickledCourse}")
with open("students/marks.text","r") as f3:
    marks=f3.read()
    print(f"please enter the mark's info: \n{marks}")
    pickledMark=pickle.dumps(courses)
    print(f"The information of pickled course is: \n{pickledMark}")
