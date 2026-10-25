# Case Study 10: Integrated Student Record Consistency Checker

## 1. Problem Statement
Validate student identifiers, names, marks, attendance, and course records. Detect duplicate roll numbers, missing fields, invalid marks or attendance, and inconsistent records.

## 2. Objectives
- Validate records using strings, lists, and tuples.
- Identify duplicate identifiers and invalid values.
- Generate a reason-wise consistency report.

## 3. Assumptions
- Each record is a tuple: roll number, name, marks, attendance, course code.
- Roll numbers must be unique and non-empty.
- Marks must be between 0 and 100, attendance between 0 and 100, and name/course code must not be empty.

## 4. Algorithm
1. Define sample student tuples.
2. Scan records and count each roll number.
3. For each record, create an error list.
4. Check duplicate roll number, missing values, marks, attendance, and course code.
5. Display VALID or INVALID with reasons.

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
COUNT occurrences of each roll number
FOR each student tuple
  SET errors to empty list
  CHECK missing fields
  CHECK roll number count > 1
  CHECK marks range 0–100
  CHECK attendance range 0–100
  CHECK course code not empty
  DISPLAY VALID if no errors; otherwise display errors
```

## 7. Python Source Code
```python
# Integrated Student Record Consistency Checker
records = [
    ("26000293", "Kusuma Priya", 92, 96, "CSE101"),
    ("26000294", "Yamuna", 78, 82, "CSE101"),
    ("26000293", "Duplicate Roll", 65, 75, "CSE102"),
    ("26000296", "", 108, 110, ""),
]

roll_numbers = []
for record in records:
    roll_numbers.append(record[0])

print("STUDENT RECORD AUDIT")
for roll, name, marks, attendance, course in records:
    errors = []
    if roll == "":
        errors.append("missing roll number")
    if roll_numbers.count(roll) > 1:
        errors.append("duplicate roll number")
    if name.strip() == "":
        errors.append("missing student name")
    if marks < 0 or marks > 100:
        errors.append("marks outside 0-100")
    if attendance < 0 or attendance > 100:
        errors.append("attendance outside 0-100")
    if course.strip() == "":
        errors.append("missing course code")

    if len(errors) == 0:
        print(roll, name, ": VALID")
    else:
        print(roll, name if name else "(no name)", ": INVALID")
        for error in errors:
            print(" -", error)
```

## 8. Test Cases
| Test | Input / Condition | Expected result |
|---|---|---|
| Valid record | Unique roll; name/course present; marks 92; attendance 96 | VALID |
| Duplicate roll | Two records use roll 26000293 | Both flagged duplicate |
| Invalid values | Marks 108; attendance 110; empty name/course | All corresponding errors reported |

## 9. Output Screenshot
![Sample output](output_screenshots/sample_output.png)

The PNG is generated from the program's captured sample run. `sample_output.txt` contains the same output as text.

## 10. Conclusion
The program audits student records and explains consistency errors. The sample records are fictional and should not be treated as official student data.
