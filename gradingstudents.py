def gradingStudents(grades):
    res = []
    for i in range(len(grades)):
        if grades[i] > 37:
            if 5 - (grades[i] % 5) < 3:
                grades[i] = ((grades[i] // 5) +1) *5
        res.append(grades[i])
    return res
