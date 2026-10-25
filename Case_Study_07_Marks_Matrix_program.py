# Student Marks Matrix Analysis
students = ["Asha", "Bharat", "Charan", "Divya"]
subjects = ["Python", "Maths", "Computing"]
marks = [
    [88, 76, 91],
    [65, 72, 68],
    [42, 48, 55],
    [95, 89, 93],
]

valid = True
for row in marks:
    for mark in row:
        if mark < 0 or mark > 100:
            valid = False

if not valid:
    print("Invalid marks: values must be from 0 to 100")
else:
    totals = []
    print("STUDENT RESULTS")
    for i in range(len(students)):
        total = sum(marks[i])
        average = total / len(subjects)
        totals.append(total)
        print(students[i], "Total:", total, "Average:", round(average, 2))

    print("\nSUBJECT AVERAGES")
    for j in range(len(subjects)):
        total = 0
        for i in range(len(students)):
            total += marks[i][j]
        average = total / len(students)
        print(subjects[j], "Average:", round(average, 2),
              "LOW AVERAGE" if average < 50 else "")

    top_index = totals.index(max(totals))
    print("\nTop performer:", students[top_index],
          "with total", totals[top_index])
