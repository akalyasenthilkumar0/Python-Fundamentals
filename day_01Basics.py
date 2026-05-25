#--------------------------------------
#Day1 Python Basic Programs
#--------------------------------------

#1.Print Statement 

print("I'm Akalya,Just started my python journey!")
print("--------------------------------")


#2.Take input and print its type

value=input("Enter:")
print("Value=",value)
print("Type=",type(value))
print("--------------------------------")

#3.Swap Two numbers(with and without temp)

#without temp

a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("The values of a and b before Swapping: a=",a,"b=",b)
a,b=b,a
print("The values of a and b after Swapping:a=",a,"b=",b)

#with temp 

a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("Before Swapping:")
print("a=",a)
print("b=",b)
temp=a
a=b
b=temp
print("After Swapping:"\n a=",a,"\n b=",b)
print("--------------------------------")

#4.Simple Calculator

a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("This is a simple calculator with basic operations. \nBasic Operations like,")
print("\na. Add"
"\nb.Subtraction"
"\nc.Multiplication"
"\nd.Division")
print("sum=",a+b)
print("difference=",a-b)
print("product=",a*b)
print("quotient=",a//b)
print("Successfully executed!!")
print("--------------------------------")

#5. Area of a Circle

r=float(input("Enter value:"))
area=3.14159*r*r
print("Area of the circle is",area)
print("-------------------------------")


#6. Temperature Conversions

#------Celsius to Fahrenheit---------

temp=float(input("Enter Temperature Value:"))
res=(temp*9/5)+32
print("Celsius to Fahrenheit=",res,"°F")










