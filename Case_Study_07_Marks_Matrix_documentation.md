# Case Study 07: Student Marks Matrix Analysis

## 1. Problem Statement
Analyse a nested list of marks for multiple students across multiple subjects. Calculate student totals and averages, subject averages, identify the top performer, and flag subjects with low average marks.

## 2. Objectives
- Use nested lists to store a marks matrix.
- Calculate row-wise and column-wise statistics.
- Identify top student and weak subjects.

## 3. Assumptions
- Marks are integers from 0 to 100.
- Every student has marks for the same subjects.
- A subject average below 50 is flagged as low.

## 4. Algorithm
1. Define student names, subject names, and marks matrix.
2. Validate each mark.
3. Calculate each student's total and average.
4. Calculate each subject's average using column positions.
5. Find top performer by total marks and flag low-average subjects.
6. Print summary.

## 5. Flowchart
```text
START
  |
LOAD INPUT / SAMPLE DATA
  |
VALIDATE INPUTS
  |
PROCESS USING CONDITIONS AND LOOPS
  |
DISPLAY RESULTS AND ERRORS
  |
END
```

## 6. Pseudocode
```text
FOR each row in marks matrix, calculate total and average
FOR each subject column, add marks across all students and calculate average
FIND student with maximum total
FOR each subject, IF average < 50, flag as low
DISPLAY all statistics
```

## 7. Python Source Code
```python
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
```

## 8. Test Cases
| Test | Input / Condition | Expected result |
|---|---|---|
| Normal matrix | All marks within 0–100 | Totals, averages, subject averages, and top performer displayed |
| Low subject average | One subject average below 50 | Subject flagged LOW AVERAGE |
| Invalid mark | Any mark = 105 | Invalid marks message |

## 9. Output Screenshot
![Sample output](output_screenshots/sample_output.png)

The PNG is generated from the program's captured sample run. `sample_output.txt` contains the same output as text.

## 10. Conclusion
The program demonstrates nested-list traversal and row-wise/column-wise calculations for academic performance analysis.
