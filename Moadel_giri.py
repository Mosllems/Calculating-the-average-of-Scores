def average():
    grade = []
    grade_2 = []
    z = 0
    print("Nomrehato vared kon va har vaqt tamom shod 0 ro vared kon")
    while True:
        score = float(input("Nomrato vared kon: "))
        if score <= 20 and score > 0:
            grade.append(score)
            zarib = int(input("Chand vahedie: "))
            if 1 <= zarib <= 3:
                z += zarib
            majmo = score * zarib
            grade_2.append(majmo)
        if score == 0:
            break
    s = sum(grade_2)
    moadel = s / z
    round(moadel, 2)
    print(f"Moadel in termet {moadel} shode")

average()