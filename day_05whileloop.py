#----------------------------------------

#day_5whileloop

#----------------------------------------


#1.Reverse of a number

n=int(input("Enter a number:"))
rev=0
while(n>0):
  digit=n%10
  rev=rev*10+digit
  n//=10
print("Reverse of the given number is",rev)


#----------------------------------------


#2.Sum of Digits 

num=int(input("Enter a number:"))
sum_diguts=0
while num>0:
   digit=num%10
   sum_digits += digit 
   num//=10
print("Sum of all digits",sum_digits")

#---------------------------------------


#3.Print 1 to N numbers

n = int(input("Enter n:"))
i=1
while i<=n:
  print(i)
  i+=1

#----------------------------------------


#4.Multiplication Table

n=int(input("Enter n:"))
i=1
while i<=10:
   print(n,"x",i,"=",n*i)
   i+=1

#---------------------------------------- 


#5.Palindrome Check 

num=int(input("Enter a number:"))
org=num
rev=0
while n>0:
   digit=num%10
   rev=rev*10+digit
   num//=10 

if (org==rev):
  print("The entered number is a Palindrome.")
else:
  print("The entered number is not a Palindrome.")

#--------------------------------------- 


#6.Password Checker

passw=""

while (passw!="hihi%22%"):
   passw=input("Enter Password:")
print("Successful") 

#----------------------------------------


#7. Number Guessing Game 

secret=12
guess=0 

while guess!=secret :
   guess = int(input("Enter a number:"))
  
  if(guess>secret):
     print("Larger number")
  elif(guess<secret):
     print("Smaller number")

print("You're Right!") 

#---------------------------------------




 
