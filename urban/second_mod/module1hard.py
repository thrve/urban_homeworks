#!/usr/bin/env python


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {"Johnny", "Bilbo", "Steve", "Khendrik", "Aaron"}
gpa = []
students_list = sorted(list(students))

for i in grades:
    k = 0
    for j in i:
        k += j
    gpa.append(k / len(i))

for i in gpa:
    for j in students_list:
        result
