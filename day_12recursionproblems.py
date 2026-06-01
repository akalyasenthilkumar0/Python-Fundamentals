#----------------------------------------------------------------------------------------------------------------
#Recursion problems
#----------------------------------------------------------------------------------------------------------------

#1.Factorial of a number 

def factorial(n):
  
    if n == 0 or n == 1:
       return 1
      
    return n * factorial(n - 1)

print("Factorial of 8 is," ,factorial(8))  

#-----------------------------------------------------------------------------------------------------------------

#2.Fibonacci Series

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci Series:", fibonacci(10), end=" ")

#----------------------------------------------------------------------------------------------------------------

#3. Sum of Digits

def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(5987))

#-----------------------------------------------------------------------------------------------------------------

#4. Reverse of a number 

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

print("Reverse of a given number:", reverse_number(9765))  

#------------------------------------------------------------------------------------------------------------------

#5. Power function 

def power(a,b):
  if b==0:
     return 1
  return a * power(a,b-1)

print("Result:", power(5,3))

#-----------------------------------------------------------------------------------------------------------------

#6. Greatest Common Divisor

 def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 12)) 
print(gcd(96,4)) 

#-----------------------------------------------------------------------------------------------------------------

#7. Tower of Hanoi

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

tower_of_hanoi(4, 'A', 'C', 'B')

#-----------------------------------------------------------------------------------------------------------------

#8. Binary Search 

def binary_search(arr, target, low, high):
    if low > high:
        return -1  

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

arr = [11,22,33,44,55,66,77,88,99,100]
target = 66
result = binary_search(arr, target, 0, len(arr)-1)

print(f"Element {target} found at index {result}")

#------------------------------------------------------------------------------------------------------------------






