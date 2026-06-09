#-----------------------------------------------------------------------------------------------------------------
#Mini Project - Expense Tracker
#-----------------------------------------------------------------------------------------------------------------

print("----------Expense Tracker----------")

expenses=[]

while True:
  print("1.Add Expense")
  print("2.View Expense")
  print("3.Total Expense")
  print("4.Exit")

choice = int(input("Enter your choice:"))

if choice == 1:
  amt=float(input("Enter Expense amount="))
  expenses.append(amt)
  print("Expense Amount added Successfully!!")

elif choice == 2:
  if len(expenses) == 0:
    print("No Expense is recorded")
  else:
    print("\nExpenses:")
    for i in expenses:
      print(i)

elif choice == 3:
  total = sum(expenses)
  print("Total Expense:", total)

elif choice == 4:
  print("----Exit----")
  break

else:
  print("Enter a Valid Choice")




  
  
  
