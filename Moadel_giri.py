def average():
    grade = []
    grade_2 = []
    z = 0
    print("Enter your scores and to exit the program enter 0 ")
    while True:
        score = float(input("Enter your score: "))
        if score <= 20 and score > 0:
            grade.append(score)
            zarib = int(input("Enter the credits: "))
            if 1 <= zarib <= 3:
                z += zarib
            majmo = score * zarib
            grade_2.append(majmo)
        if score == 0:
            break
    s = sum(grade_2)
    moadel = s / z
    round(moadel, 2)
    print(f"The average of this semester is {moadel}")

average()