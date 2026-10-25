# Case Study 01: University Scholarship Allocation

## 1. Problem Statement
Design a program to assess scholarship applicants using aggregate marks, minimum subject marks, attendance, and annual family income. Eligible applicants are ranked using aggregate marks, then attendance, then lower income as tie-breakers.

## 2. Objectives
- Validate applicant data against stated eligibility rules.
- Calculate eligibility and explain rejection reasons.
- Rank eligible applicants deterministically.

## 3. Assumptions
- Aggregate and subject marks are percentages from 0 to 100.
- Minimum aggregate is 80%, minimum subject mark is 70%, attendance is at least 85%, and annual family income is at most ₹300,000.
- Sample data is illustrative and not an official scholarship policy.

## 4. Algorithm
1. Start and define sample applicant records.
2. For each applicant, check aggregate, all subject marks, attendance, and income.
3. Store the reasons for any failed conditions.
4. Collect eligible applicants and sort by aggregate descending, attendance descending, income ascending.
5. Display eligibility, reasons, and the ranked list.

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
SET applicants to sample records
FOR each applicant
  CREATE empty reasons list
  CHECK aggregate, each subject mark, attendance, and income
  IF any condition fails, add reason to reasons
  IF reasons is empty, add applicant to eligible list
  ELSE display applicant and reasons
SORT eligible by aggregate descending, attendance descending, income ascending
DISPLAY ranked eligible list
```

## 7. Python Source Code
```python
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
```

## 8. Test Cases
| Test | Input / Condition | Expected result |
|---|---|---|
| Asha | 88 aggregate; all subjects ≥70; attendance 92; income 240000 | Eligible; appears in ranking |
| Charan | Aggregate 79 | Not eligible: aggregate below 80% |
| Divya | Attendance 81 | Not eligible: attendance below 85% |

## 9. Output Screenshot
![Sample output](output_screenshots/sample_output.png)

The PNG is generated from the program's captured sample run. `sample_output.txt` contains the same output as text.

## 10. Conclusion
The program applies multiple eligibility conditions and ranks only qualified applicants. Its rules are configurable and should be replaced with the institution's official policy when required.
