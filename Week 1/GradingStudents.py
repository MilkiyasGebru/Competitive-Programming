def gradingStudents(grades):
    # Write your code here
    newgrades = []
    for grade in grades:
        if grade < 38 :
            newgrades.append(grade)
        else :
            num = grade // 5
            next_mul = (num+1)*5
            if next_mul-grade < 3 :
                newgrades.append(next_mul)
            else :
                newgrades.append(grade)     
    return newgrades 
