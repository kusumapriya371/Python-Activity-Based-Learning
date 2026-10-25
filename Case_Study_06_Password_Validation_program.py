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
