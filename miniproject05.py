#-----------------------------------------------------------------------------------------------------------------
#miniproject-05:Student Grade Calculator
#-----------------------------------------------------------------------------------------------------------------

print(f"Student Grade Calculator")

#name of the student
name=str(input("Enter name of the Student:"))

#total number of subjects
no_of_subjects= int(input("Enter the number of Subjects:"))

print(f"Marks Scored by {name}: \n")

#marks scored by the student
marks=[]

for i in range(5):
    mark=int(input("Enter mark:"))
    marks.append(mark)
    
print(marks)

#total marks scored by the student
def total_marks(marks):
    total=sum(marks)
    return(total)
result=total_marks(marks)
print(f"Total Marks Scored by {name}:",result)

#calculating average 
def average(total):
    avg=total//no_of_subjects
    return avg
total=total_marks(marks)
avg = average(total)
print("Average = ",avg)

#finding the grade secured
def Calculate_grade(avg):

    if avg>85 :
        return("Grade:A")
    elif avg<=85 and avg>=75:
        return("Grade:B")
    elif avg<75 and avg>=60:
        return("Grade:C")
    elif avg<60 and avg>=50:
        return("Grade:D")
    else:
        return("Fail")
    
grade=Calculate_grade(avg)
print(f"Grade of {name}: \n", grade)

