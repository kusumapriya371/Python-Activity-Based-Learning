# Case Study 04: Attendance Recovery Computation

## 1. Problem Statement
Calculate a student's current attendance percentage and determine the minimum number of consecutive classes the student must attend to reach a required attendance threshold.

## 2. Objectives
- Calculate current attendance accurately.
- Use a loop to find the minimum future classes required.
- Handle already-eligible and impossible inputs.

## 3. Assumptions
- Classes attended and total classes are non-negative integers; attended cannot exceed total.
- The required attendance threshold is 75%.
- Future scenario assumes every additional class is attended.

## 4. Algorithm
1. Set attended classes, total classes, and threshold.
2. Validate the input values.
3. Calculate current attendance percentage, or zero if total is zero.
4. If current percentage meets threshold, required classes are zero.
5. Otherwise increment future attended and total classes until the threshold is reached.
6. Display percentage and minimum classes needed.

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
INPUT attended, total
IF attended < 0 OR total < 0 OR attended > total, DISPLAY invalid input
ELSE calculate current percentage
SET extra = 0
WHILE (attended + extra) / (total + extra) < threshold
  extra = extra + 1
DISPLAY current percentage and extra
```

## 7. Python Source Code
```python
# Attendance Recovery Computation
attended = 42
total = 60
threshold = 75

if attended < 0 or total < 0 or attended > total:
    print("Invalid attendance data")
elif total == 0 and attended == 0:
    print("No classes recorded yet")
else:
    current = attended * 100 / total
    extra = 0
    while (attended + extra) * 100 / (total + extra) < threshold:
        extra += 1
    print("Current attendance:", round(current, 2), "%")
    if extra == 0:
        print("Already eligible.")
    else:
        print("Consecutive classes to attend:", extra)
    print("Attendance after those classes:",
          round((attended + extra) * 100 / (total + extra), 2), "%")
```

## 8. Test Cases
| Test | Input / Condition | Expected result |
|---|---|---|
| Already eligible | Attended 48 of 60 | 80%; required extra classes = 0 |
| Needs recovery | Attended 42 of 60 | 70%; required extra classes = 12 |
| Invalid | Attended 65; total 60 | Invalid attendance data |

## 9. Output Screenshot
![Sample output](output_screenshots/sample_output.png)

The PNG is generated from the program's captured sample run. `sample_output.txt` contains the same output as text.

## 10. Conclusion
The program uses a loop to find the smallest number of future attended classes that reaches the target percentage.
