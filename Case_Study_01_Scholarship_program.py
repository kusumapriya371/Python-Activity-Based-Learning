# University Scholarship Allocation
# Sample data; thresholds are assumptions for this assignment.
applicants = [
    ("Asha", 88, [82, 91, 79], 92, 240000),
    ("Bharat", 84, [76, 72, 81], 88, 180000),
    ("Charan", 79, [90, 86, 82], 95, 150000),
    ("Divya", 91, [92, 88, 94], 81, 200000),
]

eligible = []
for name, aggregate, subjects, attendance, income in applicants:
    reasons = []
    if aggregate < 80:
        reasons.append("aggregate below 80%")
    for mark in subjects:
        if mark < 70:
            reasons.append("a subject mark below 70%")
            break
    if attendance < 85:
        reasons.append("attendance below 85%")
    if income > 300000:
        reasons.append("income above Rs.300000")

    if len(reasons) == 0:
        eligible.append((name, aggregate, attendance, income))
        print(name, ": ELIGIBLE")
    else:
        print(name, ": NOT ELIGIBLE -", ", ".join(reasons))

eligible.sort(key=lambda item: (-item[1], -item[2], item[3]))
print("\nScholarship ranking:")
for rank, applicant in enumerate(eligible, start=1):
    print(rank, applicant[0], "Aggregate:", applicant[1],
          "Attendance:", applicant[2], "Income:", applicant[3])
