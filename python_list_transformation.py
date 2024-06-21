# task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)

grades_average = sum(grades)/10
print(grades_average)

grades[7] = "Failed"
grades[8] = "Failed"
grades[9] = "Failed"
print(grades)