#--------------------------------------
#day3_conditionals
#--------------------------------------


#1.Grade calculator 

name=str(input("Enter name:"))
English=int(input("Enter marks in English="))
Maths=int(input("Enter marks in Maths="))
Science=int(input("Enter marks in Science="))
avg=(English+Maths+Science)//3
print("Average Marks=",avg)
print("Calculating the Grade:")
if (avg>=85):
    print(" Grade:'A' ")
elif (avg>=65 and avg<85):
    print("Grade:'B' ")
elif (avg>=45 and avg<65):
    print("Garde:'C' ")
else:
    print("Failed!")
print("----------------------------------")


#2.Vowel_Consonant

c=str(input("Enter character:"))
vowels='AEIOUaeiou'
if(c in vowels):
    print("The given character is a vowel.")
else:
    print("The given character is a consonant.")
print("-----------------------------")


#3.Triangle validity 

print("The sides of a Triangle:")

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if((a+b)>c and (b+c)>a and (a+c)>b):
   print("The given sides form a valid    Triangle.")
else:
   print("It's not a valid Triangle")

print("-------------------------------")



#4.Electricitybill

units=int(input("Enter units:"))
if units<=100:
    print("Bill=₹0")
elif(units>100 and units<=200):
    print("Bill=₹",(units-100)*5)
elif(units>200):
    print("Bill=₹",((100*5)+(units-200)*10))
else:
    print("Invalid")
print("------------------------------")


#5.Simple login system

user_name=input("Set username:")
pass=input("Set password:")

print("\nLogin")

username=input("Username:"))
password=input("Password:")

if(user_name==username and pass==password):
  print(" Login Successful! ")
elif(user_name!=username):
  print("Invalid Username")
else:
  print("Invalid Password")


print("--------------------------------")



#6.Discount calculator 

print("Discount Calculator")
amt=int(input('Enter the total amount purchased:₹ '))
if amt >=5000:
    discount=(5000*(50/100))
    final_amt= amt-discount
    print("After discount of 50%: ₹ ",final_amt)
elif amt>=2000:
    discount=(2000*(20/100))
    final_amt= amt-discount
    print("After discount of 20%: ₹ ",final_amt)
else:
    print("No discounts for purchase less than ₹2000.")

print("-------------------------------")


