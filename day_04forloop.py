#---------------------------------------

#day4_forloop

#---------------------------------------


#1.print numbers from 1 to 100

for i in range(1,101,1):
   print("Numbers from 1 to 100:",i)

print("-----------------------------")


#2.sum of N numbers

n=int(input("Enter n:"))
sum_n=n*(n+1)//2
print("The sum of N numbers:",sum_n)


n=int(input("Enter n:"))
sum_n=0
for i in range(1,n+1):
  sum_n += i
print("Sum of N numbers:",sum_n)

print("------------------------------")


#3.print even numbers from 2 to 20

for i in range(2,22,2):
  print("even numbers from 2 to 20:",i)

print("-----------------------------")


#4.print all the letters in your name

name=str(input("Enter name:"))
for n in name:
  print("letters=",n)

print("----------------------------")


#5.factorial of a number

n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
   fact*=i
print("Factorial of a given number %d is %d",%(n,fact)) 

print("-----------------------------")


#6.Fibonacci Series

terms=int(input("Enter number of terms:"))
print("Fibonacci Series")
a,b=0,1
print(a,b,end=" ")
for i in range(terms):
   c=a+b
   print(c,end=" ")
   a=b
   b=c

print ("-------------------------------") 


#7.Armstrongnumber

print("Armstrong number demo")
num=int(input("Enter number:"))
n=num
digits=len(str(num))
sum=0
while n>0:
   digit=n%10
   sum=sum+digit**digits
   n=n//10
if(sum == num):
    print("Yes It is an Armstrong number.")
else:
    print("Its not an Armstrong number.")
print("------------------------------")


#8.Primecheck

n=int(input("Enter number:"))
for i in range(2,n+1):
     if(n%i==0):
          print("It is not a prime number")
          break
else:
     print("It is prime number")
print("----------------------------")
    

