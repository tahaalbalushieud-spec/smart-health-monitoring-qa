## Cyclomatic Complexity – FR1

Number of decision points:
1. Loop condition
2. age >= 45
3. BMI >= 30
4. BMI >= 25
5. fastingGlucose >= 126
6. fastingGlucose >= 100
7. familyHistory == 1
8. riskScore >= 6
9. riskScore >= 3

Cyclomatic Complexity:
V(G) = 9 + 1 = 10

---

## Independent Paths

P1: age < 45, BMI < 25, glucose < 100, no family history → Low  
P2: age ≥ 45 only → Medium  
P3: BMI ≥ 25 and glucose < 100 → Medium  
P4: BMI ≥ 30 and glucose ≥ 126 → High  
P5: glucose ≥ 100 but < 126 → Medium  
P6: family history = 1 with low BMI → Medium  
P7: age ≥ 45 and BMI ≥ 30 → High  
P8: glucose ≥ 126 only → High  
P9: age ≥ 45 and family history = 1 → Medium  
P10: all risk factors high → High
