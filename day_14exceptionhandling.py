#----------------------------------------------------------------------------------------------------------------
#day 14-Exception Handling
#----------------------------------------------------------------------------------------------------------------

#1.try and except

try:
  num=int(input("Enter a number:"))
  print(num)
except ValueError:
  print("Please Enter a valid integer.")

#------------------------------------------------------------------------------------------------------------------

#2.division by zero

try:
  a=int(input())
  b=int(input())
  res = a/b
  
  print("Result:" ,res)
  
except ZeroDivisionError:
  print("Cannot divide by zero.")
  
#------------------------------------------------------------------------------------------------------------------

#3.Square number with exception handling

try:
  a = int(input("Enter a number:"))
  sq = a*a
  print("Square of the given number:",sq)
  
except ValueError:
  print("Invalid Input")
  print("Enter a Valid Input.")

#--------------------------------------------------------------------------------------------------------------------

#4.Multiple Exceptions

try: 
  num = [100,200,300,400,500]

  index = int(input("Enter Index:"))
  print("Index=", num[index])

except ValueError:
  print("Enter a Valid Input.")

except IndexError:
  print("Index out of range.")

#---------------------------------------------------------------------------------------------------------------------

#5.Positive number check with else block

try:
  num = int(input("Enter a number:"))

except ValueError:
  print("Invalid Input")
  print("Please Enter a valid input")

else:
  print("You Entered:", num)
  
  if (num>0):
    print("The given number is Positive.")

#--------------------------------------------------------------------------------------------------------------------

#6. Age Validator with finally

try:
  age = int(input("Enter age:"))

except ValueError:
  print("Invalid Input")

else:
  print("The Age of the user is", age)

  if (age >= 18):
    print("The User is Eligible for Voting")

  else:
    print("OOPS!! The User is not Eligible for Voting")

finally:
  print("Program Finished")

#---------------------------------------------------------------------------------------------------------------------

#7. Age validator with raise

try:
  age=int(input("Enter age:"))

  if age < 0:
    raise ValueError("Age cannot be negative")

 print("Age:", age)

except ValueError as e:
 print(e)

#---------------------------------------------------------------------------------------------------------------------
    
    
