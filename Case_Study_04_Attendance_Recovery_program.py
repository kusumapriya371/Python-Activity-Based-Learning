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
