#-------------------------------------

#Miniproject:"Menu-driven program"

#-------------------------------------

print("This is my Mini Project 1
\nTitle: Menu-driven program")

print("Enter the Options:\n1. Addition \n2. Subtraction \n3. Multiplication \n4.Division")

choice=int(input("Select your choice:"))

if choice not in (1,2,3,4):
  print("Invalid choice")
else:
  num1=float(input("Enter the first number:"))
  num2=float(input("Enter the second number:"))

if(choice==1):
  res= num1+num2
  print("Sum=",res)

elif(choice==2):
  if(num1>num2):
    res=num1-num2
    print("Difference=",res)
  else:
    res=num2-num1
    print("Difference=",res)

elif(choice==3):
   res=num1*num2
   print("Product=",res)

else:
   if(num2!=0):
      res=(num1/num2)
      print("Quotient=",res)
   else:
      print("Division is not possible!")

print("Successfully executed!")

print("---------------------------------")

