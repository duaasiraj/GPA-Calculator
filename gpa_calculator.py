weighted_scores = []
course_scores = []

def testGPACalculator(marks, totalmarks):
    percentage = (marks / totalmarks) * 100
    if percentage >= 86:
        gpa = 4.00
        grade = 'A'
    elif percentage >= 82:
        gpa = 3.67
        grade = 'A-'
    elif percentage >= 78:
        gpa = 3.33
        grade = 'B+'
    elif percentage >= 74:
        gpa = 3.00
        grade = 'B'
    elif percentage >= 70:
        gpa = 2.67
        grade = 'B-'
    elif percentage >= 66:
        gpa = 2.33
        grade = 'C+'
    elif percentage >= 62:
        gpa = 2.00
        grade = 'C'
    elif percentage >= 58:
        gpa = 1.67
        grade = 'C-'
    elif percentage >= 54:
        gpa = 1.33
        grade = 'D+'
    elif percentage >= 50:
        gpa = 1.00
        grade = 'D'
    else:
        gpa = 0.00
        grade = 'F'
    return gpa, grade, percentage

def calculate_course_gpa(weighted_scores):
    total_weight = 0
    weighted_total = 0
    for score, weight in weighted_scores:
        total_weight += weight
        weighted_total += score * weight
    coursepercentage = weighted_total / total_weight
    if coursepercentage >= 86:
        course_gpa = 4.00
        course_grade = 'A'
    elif coursepercentage >= 82:
        course_gpa = 3.67
        course_grade = 'A-'
    elif coursepercentage >= 78:
        course_gpa = 3.33
        course_grade = 'B+'
    elif coursepercentage >= 74:
        course_gpa = 3.00
        course_grade = 'B'
    elif coursepercentage >= 70:
        course_gpa = 2.67
        course_grade = 'B-'
    elif coursepercentage >= 66:
        course_gpa = 2.33
        course_grade = 'C+'
    elif coursepercentage >= 62:
        course_gpa = 2.00
        course_grade = 'C'
    elif coursepercentage >= 58:
        course_gpa = 1.67
        course_grade = 'C-'
    elif coursepercentage >= 54:
        course_gpa = 1.33
        course_grade = 'D+'
    elif coursepercentage >= 50:
        course_gpa = 1.00
        course_grade = 'D'
    else:
        course_gpa = 0.00
        course_grade = 'F'

    return coursepercentage, course_gpa, course_grade

def calculate_sgpa(course_scores):
    total_credits = 0
    weighted_gpa_total = 0
    for gpa, credits in course_scores:
        total_credits += credits
        weighted_gpa_total += gpa * credits
    sgpa = weighted_gpa_total / total_credits
    return sgpa
try:
    while True:
        anothercourse = input("Do you wanna add a course? (yes or no): ")
        if anothercourse.lower() != 'yes':
            break
        weighted_scores = []  
        credit_hours = float(input("Enter the credit hours for the course: "))
        while True:
            anothertest=input("Do you want to add a test?(yes / no)")
            if anothertest.lower()!="yes":
                break
            TotalMarks = float(input("Enter total marks for your test: "))
            Yourmarks = float(input("Enter your score for the test: "))
            weightage = float(input("Enter weightage: "))
            
            gpa, grade, percentage = testGPACalculator(Yourmarks, TotalMarks)
            print("GPA =", round(gpa,3), "\nGrade =", grade, "\nPercentage =", round(percentage,3))
            
            weighted_scores.append((percentage, weightage))
        
        percent, course_gpa, course_grade = calculate_course_gpa(weighted_scores)
        print("For the course:")
        print("Weighted Percentage =", round(percent,3))
        print("Course GPA =", round(course_gpa,3))
        print("Course Grade =", course_grade)
        course_scores.append((course_gpa, credit_hours))

    if len(course_scores) > 0:
        sgpa = calculate_sgpa(course_scores)
        print("\nSGPA for the semester =", round(sgpa,3))

    input("Press Enter to exit...")
except:
    IOError=print("Invalid input")