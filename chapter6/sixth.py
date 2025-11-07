# <<<<<<<<<<Conditional Expression>>>>>>>>>>
# 1. Write a program to find the greatest of four numbers entered by the user. 
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# c = int(input("Enter third number:"))
# d = int(input("Enter fourth number:"))
# if(a>b and a>c and a>d):
#     print(f"{a} is greater element")
# elif(b>c and b>d):
#     print(f"{b} greater element")    
# elif(c>d):
#     print(f"{c} is the greater element")    
# else:
# print("d is greater element")
          
# <<<<<<By Using Ternary Operator>>>>>>
# syntax: x if condition else y
# max_element = a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d
# print(max_element)

# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.
# s1 = int(input("Enter the physics marks: "))
# s2 = int(input("Enter the chemisrty marks: "))
# s3 = int(input("Enter the Maths marks: "))
# total = s1+s2+s3
# Percentage = (s1+s2+s3)/3

# if(s1>=33 and s2>=33 and s3>=33) and (Percentage >= 40):
#     print("🎉 Passed")
# else:
#     print("❌ failed")    

# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 
# spam_list = ["make a lot of money", "buy now", "subscribe this", "click this"]
# comment = input("enter the comment: ").lower()
# is_spam = False
# for keyword in spam_list:
#       if keyword in comment:
#             is_spam = True
#             break
# if is_spam:
#       print("⚠️ This comment is spam!")      
# else:
#       print("✅ This comment is safe.")      

# 4. Write a program to find whether a given username contains less than 10 
# characters or not. 
# username = input("Enter the name: ")
# print("char less than 10") if len(username)<10 else print("char not less than 10")
# if(len(username)<10):
#     print("char less than 10")
# else:
#     print("char not less than 10")  

# 5. Write a program which finds out whether a given name is present in a list or not. 
# my_list = ["aditya", "thakurji", "singhsahab", "sardarji"]
# name = input("enter the name: ").lower()
# for item in my_list:
#     if item == name:
#         print("present in list")
#         break
# else:
#     print("not present in list")  
#  
# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50  => F 
# a = int(input("enter the phy marks: "))
# b = int(input("enter the chem marks: "))
# c = int(input("enter the math marks: "))
# total = (a+b+c)/3
# if total >= 90:
#     print("Excellent")
# elif total >= 80:
#     print("A")
# elif total >= 70:
#     print("B")
# elif total>=60:
#     print("C")   
# elif total>=50:
#     print("D") 
# else:
#     print("F")    

# 7. Write a program to find out whether a given post is talking about “Harry” or not. 
# s = input("enter post: ")
# words = s.split()
# for word in words:
#     # Strip punctuation and convert to lowercase
#     clean_word = word.strip(".,!?").lower()
#     if clean_word == "harry":
#         print("yes")
#         break
# else:
#     print("No")
   
