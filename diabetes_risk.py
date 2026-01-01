def diabetes_risk(age, bmi, glucose, family_history):
    if age <= 0 or bmi <= 0 or glucose <= 0:
        return "INVALID"

    score = 0

    if age >= 45:
        score += 2

    if bmi >= 30:
        score += 2
    elif bmi >= 25:
        score += 1

    if glucose >= 126:
        score += 3
    elif glucose >= 100:
        score += 1

    if family_history == 1:
        score += 1

    if score >= 6:
        return "HIGH"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "LOW"


# Test cases (قبل التصحيح)
tests = [
    (30, 22, 90, 0, "LOW"),
    (50, 31, 130, 1, "HIGH"),
    (45, 25, 100, 0, "MEDIUM"),
    (-1, 25, 100, 0, "INVALID")   # حالة خاطئة
]

defects = 0

for i, t in enumerate(tests, start=1):
    result = diabetes_risk(t[0], t[1], t[2], t[3])
    if result != t[4]:
        defects += 1
    print(f"Test {i}: Expected={t[4]}, Got={result}")

print("Defects found:", defects)
print("Total tests:", len(tests))
