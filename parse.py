import csv
from pprint import pprint
import sys

for i in range(1, 3):
    w = str(i)
    with open("Sem" + w + ".csv", "r") as f:
        courses = list(csv.reader(f))[1:]
        course_names = [i[0] for i in courses]
        names = []
        for i in sorted(course_names):
            course_numbers = i.split(' ')[0]
            course_name = " ".join(i.split(' ')[1:])
            names.append(f"<option value=\"{i}\"></option>")
            with open(f"Schedule\\Semester" + w + f"\\{course_numbers}.txt", "w") as f2:
                f2.write(course_name + "\n")
                for meetings in set([m[-1] for m in filter(lambda x: x[0]==i, courses)]):
                    f2.write(meetings + "\n")
        
        with open("SemesterOptions.txt", "a") as f:
            f.write("".join(sorted(list(set(names))))+"\n")

for i in range(1, 3):
    w = str(i)
    with open("Sem" + w + ".csv", "r") as f:
        courses = list(csv.reader(f))[1:]
        course_names = [i[0] for i in courses]
        names = []
        for i in sorted(course_names):
            course_numbers = i.split(' ')[0]
            course_name = " ".join(i.split(' ')[1:])
            with open(f"Custom{w}.txt", "a") as f2:
                for meetings in set([m[-1] for m in filter(lambda x: x[0]==i, courses)]):
                    f2.write(f"<option value=\"{course_numbers} - {meetings}\"></option>")