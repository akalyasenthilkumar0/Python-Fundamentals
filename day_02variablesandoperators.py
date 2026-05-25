#------------------------------------
#day2_variablesandoperators
#------------------------------------

#1.Even or Odd

num=int(input("Enter the number :"))
if(num%2==0):
    print("The given number is even.")
else:
    print("The given number is odd.")
print("------------------------------")


#2.Positive/Negative/Zero

n=int(input("Enter the value:"))
if(n>0):
  print("The given number is Positive.")
elif(n<0):
  print("The given number is Negative.")
else:
  print("The given number is Zero.")
print("------------------------------")


#3.Largest of 3 NUMBERS 

x=int(input("Enter x="))
y=int(input("Enter y="))
z=int(input("Enter z="))
if(x>y and x>z):
  print("Largest number is",x)
elif(y>x and y>z):
  print("Largest number is",y)
else:
  print("Largest number is",z)
print("-----------------------------")


#4.Leap year check

year=int(input("Enter year:"))
if(year%4==0):
   print("It is a leap year.")
else:
   print("It is not a leap year.")
print("----------------------------")



#5.Bitwise operators

a = 5
b = 3

print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("------------------------------")


#6.Logical and Bitwise Operator 

x = int(input("Enter x:"))
y = 3

print("Logical and:", (x > 2) and (y > 1))
print("Bitwise AND:", x & y)
print("-------------------------------")


#7.Operator Precedence example 

print("Example of operator Precedence:")
x=15*(6+7(9*(4-1))/5)/3
print("Answer=",x)


#8.Increment without using +

n=int(input("Enter the number:"))
n+=1
print("After Increment with assignment operator:")

#---------------------------------------

n=int(input("Enter the number:"))
n=n-(-1)
print("After Increment with using +:",n)
print("--------------------------------")



