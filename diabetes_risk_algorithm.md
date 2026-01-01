# FR1 – Diabetes Risk Prediction Algorithm

## Purpose
The purpose of this algorithm is to predict the diabetes risk level of a user based on health-related input data such as age, BMI, fasting glucose level, and family medical history. The algorithm calculates a risk score and classifies the risk as Low, Medium, or High.

---

## Algorithm (Pseudo-code)

START

INPUT numberOfUsers

FOR each user from 1 to numberOfUsers DO

    INPUT age
    INPUT BMI
    INPUT fastingGlucose
    INPUT familyHistory   // 1 = Yes, 0 = No

    riskScore = 0

    IF age >= 45 THEN
        riskScore = riskScore + 2
    ENDIF

    IF BMI >= 30 THEN
        riskScore = riskScore + 2
    ELSE IF BMI >= 25 THEN
        riskScore = riskScore + 1
    ENDIF

    IF fastingGlucose >= 126 THEN
        riskScore = riskScore + 3
    ELSE IF fastingGlucose >= 100 THEN
        riskScore = riskScore + 1
    ENDIF

    IF familyHistory == 1 THEN
        riskScore = riskScore + 1
    ENDIF

IF riskScore >= 7 THEN
    riskLevel = "High"

    ELSE IF riskScore >= 3 THEN
        riskLevel = "Medium"
    ELSE
        riskLevel = "Low"
    ENDIF

    DISPLAY riskLevel

END FOR

END

