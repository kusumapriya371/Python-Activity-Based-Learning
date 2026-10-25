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
