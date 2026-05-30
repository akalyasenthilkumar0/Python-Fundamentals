#---------------------------------------------------------------------------------------------------------------------------

#day_11functions.py

#---------------------------------------------------------------------------------------------------------------------------

#1.Create and call functions 

def wish():
    print("Welcome to Python")

wish()

#----------------------------------------------------------------------------------------------------------------------------

#2.Functions with paramaters 

def greet(name):
   print("Welcome," name)

greet("Ajith")

#----------------------------------------------------------------------------------------------------------------------------

#3.Function with return value

def add(a,b):
  return a+b 

res= add(11,22)

print("Sum of two numbers is",res)

#----------------------------------------------------------------------------------------------------------------------------

#4. even/odd using function 

num=int(input("Enter a number:"))

def even_odd(num):
   if num%2==0:
     return("Even number")
   else:
     return("Odd number")

res= even_odd(num)
print(res)

#----------------------------------------------------------------------------------------------------------------------------

#5.Factorial using function 

num = int(input("Enter a number: "))

def fact(num):
    fact = 1

    if num <= 1:
        return 1

    for i in range(1, num+1):
        fact *= i

    return fact

res = fact(num)

print("Factorial of the given number is:", res)

#-----------------------------------------------------------------------------------------------------------------------------

#6. Prime check 

def prime(num):

    if num <= 1:
        return "Not Prime"

    for i in range(2, num):
        if num % i == 0:
            return ("Not Prime")

        else:
            return ("Prime Number")

result = prime(78)

print(result)

#----------------------------------------------------------------------------------------------------------------------------

#7. lambda function

add = lambda a, b: a + b
result=add(10, 20)
print("Sum:",result)

#-----------------------------------------------------------------------------------------------------------------------------

#8. square of a number 

sq=lambda t:t*t
res=sq(56)
print("Square of 56:",res)

#-----------------------------------------------------------------------------------------------------------------------------

#9.Recursive function

num=int(input("Enter a number:"))

def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num - 1)

result=factorial(num)

print("Factorial=",result)

#------------------------------------------------------------------------------------------------------------------------------






  
