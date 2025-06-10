

all_student_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\all_students.txt"

passed_student_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\passed_students.txt"


all_student_set=set()

passed_students_set=set()


with open(all_student_path,"r") as fr:

    for line in fr:

        all_student_set.add(line.rstrip("\n"))


with open(passed_student_path,"r")as fr2:

    for line in fr2:

        passed_students_set.add(line.rstrip("\n"))

failed_students=all_student_set.difference(passed_students_set)

print(failed_students)



