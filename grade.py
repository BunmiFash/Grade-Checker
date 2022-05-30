def grade(marks):
    if marks >= 90:
        return ("Your grade is A")

    elif marks >= 80: 
        return ("Your grade is B")   

    elif marks >= 70:
        return ("Your grade is C") 

    elif marks >= 60:
        return ("Your grade is D") 
    
    else:
        return ("Your grade is F") 


student_marks = int(input("Marks = "))
x = grade(student_marks)
print(x)