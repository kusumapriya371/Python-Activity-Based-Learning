# Case Study 06: Password Policy Validation Engine

## 1. Problem Statement
Evaluate sample password strings against minimum length, uppercase, lowercase, digit, special-character, repeated-character, and prohibited-substring rules. Explain every failed condition.

## 2. Objectives
- Validate passwords using string operations and loops.
- Report all failed rules rather than stopping at the first failure.
- Classify a password as accepted or rejected.

## 3. Assumptions
- Minimum length is 8 characters.
- A password must contain uppercase, lowercase, a digit, and one special character from !@#$%&*.
- Three identical consecutive characters are prohibited; the substring 'password' is prohibited without case sensitivity.

## 4. Algorithm
1. Set sample passwords and policy rules.
2. For each password, create a list of failures.
3. Check length and character categories.
4. Check prohibited substring and three consecutive identical characters.
5. Print accepted or rejected and list failures.

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
FOR each password
  SET failures to empty list
  CHECK length >= 8
  SCAN characters for uppercase, lowercase, digit, and special character
  CHECK prohibited substring
  CHECK every group of 3 consecutive characters
  IF failures empty, DISPLAY ACCEPTED
  ELSE DISPLAY REJECTED and failures
```

## 7. Python Source Code
```python
# Password Policy Validation Engine
passwords = ["Kusuma@2026", "abc123", "Strong!!!9A", "password#9A"]

for password in passwords:
    failures = []
    if len(password) < 8:
        failures.append("must contain at least 8 characters")

    upper = lower = digit = special = False
    for ch in password:
        if ch.isupper():
            upper = True
        if ch.islower():
            lower = True
        if ch.isdigit():
            digit = True
        if ch in "!@#$%&*":
            special = True

    if not upper:
        failures.append("needs an uppercase letter")
    if not lower:
        failures.append("needs a lowercase letter")
    if not digit:
        failures.append("needs a digit")
    if not special:
        failures.append("needs a special character from !@#$%&*")
    if "password" in password.lower():
        failures.append("contains prohibited word 'password'")

    repeated = False
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            repeated = True
    if repeated:
        failures.append("contains three identical consecutive characters")

    if len(failures) == 0:
        print(password, ": ACCEPTED")
    else:
        print(password, ": REJECTED")
        for failure in failures:
            print(" -", failure)
```

## 8. Test Cases
| Test | Input / Condition | Expected result |
|---|---|---|
| Strong password | Kusuma@2026 | Accepted |
| Too short | abc123 | Rejected for length and missing character categories |
| Repeated characters | Strong!!!9A | Rejected for three consecutive identical characters |
| Prohibited substring | password#9A | Rejected because the prohibited substring 'password' is present |

## 9. Output Screenshot
![Sample output](output_screenshots/sample_output.png)

The PNG is generated from the program's captured sample run. `sample_output.txt` contains the same output as text.

## 10. Conclusion
The program demonstrates string methods, character scanning, and multiple validation rules. It is an educational example and is not a complete production security checker.
