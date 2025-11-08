# <<<<<<<<<<Loops In Python>>>>>>>>>>
# 1. Write a program to print multiplication table of a given number using for loop. 
# n = int(input("Enter the number: "))
# for i in range(1, 11):
#       print(f"2 X {i} = {n * i}")

#  2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S. 
# l = ["Harry", "Soham", "Sachin", "Rahul"]     
# for item in l:
    # for ch in item:
    #     if ch=="S":
    #         print(f"greet:",item)
# this is not perfect for because when there is in name 'S' present other than
#  starting then it greet many time to that name.
#********2nd solution********
# l = ["Harry", "Soham", "Sachin", "Rahul", "Saraswati"] 
# for item in l:
#     if item.startswith("S"):
#        print("greet: ",item)

# 3. Attempt problem 1 using while loop. 
# n = int(input("Enter the number: "))
# i=1
# while i<11:
#     print(f"2 X {i} = {n * i}")
#     i = i + 1

# 4. Write a program to find whether a given number is prime or not.
# n = int(input("Enter the number: "))
# ct=0
# for i in range(1,10):
#   if n%i==0:
#     ct = ct+1  
# if(ct==2):
#   print("Prime")            
# else:
#   print("not prime")  

# 5. Write a program to find the sum of first n natural numbers using while loop. 
# *****By using formula*****
# n = int(input("Enter the number: "))
# print((n*(n+1))//2)
# sum=0
# i=1
# while i<=n:
#     sum = sum + i
#     i = i + 1
# print(sum)   

# check 6. Write a program to calculate the factorial of a given number using for loop. 
# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
# print("Factorial =", fact)

# 7. Write a program to print the following star pattern. 
# * 
# *** 
# ***** for n = 3 /
# <<<Mantra!!>>>
# 1.Nested Loops
# 2.Outer loops = number of rows
# 3.inner loops = focus on column,how to connect column with rows
# i=1
# for i in range(1,4):
#     for j in range(1,2*i):
#          print("*",end="")
#     print()        

# 8. Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3
# for i in range(1,4):
#      for j in range(1,i+1):
#         print("*",end="")
#      print()    

# 9. Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * 
# n = 3
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == 1 or i == n or j == 1 or j == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
    # print()
# 10. Write a program to print multiplication table of n using for loops in reversed 
# order. 
# n=2
# i=10
# for i in range(10,0,-1):
# while i>0:
    # print(f"{n} x {i} = {n*i}")
    # i=i-1
