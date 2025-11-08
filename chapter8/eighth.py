# <<<<<<<<<<Functions & Recursions>>>>>>>>>>
# 1. Write a program using functions to find greatest of three numbers. 
# 2. Write a python program using function to convert Celsius to Fahrenheit. 
# 3. How do you prevent a python print() function to print a new line at the end. 
# 4. Write a recursive function to calculate the sum of first n natural numbers. 
# 5. Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3 
# 6. Write a python function which converts inches to cms. 
# 7. Write a python function to remove a given word from a list ad strip it at the same 
# time. 
# 8. Write a python function to print multiplication table of a given number. 
# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c
# print(greatest(4,-1,99))    

# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# # Taking user input
# c = float(input("Enter temperature in Celsius: "))
# f = celsius_to_fahrenheit(c)
# print(f"{c}°C = {f}°F")

# 👉 Use print(..., end="") to prevent a newline at the end of the print statement.
# end="" tells Python not to move to a new line after printing.

# def sum_of_natural_number(num):
#        if num==0:
#         return 0
#        else:
#            return num + sum_of_natural_number(num - 1)
            
# print(sum_of_natural_number(5))

# def print_pattern(n):
#     for i in range(n, 0, -1):   # start from n down to 1
#         print("*" * i) → repeats * i times on each line

# print_pattern(3)

# def inches_to_cm(inches):
#     cm = inches * 2.54
#     return cm

# # Taking user input
# inches = float(input("Enter length in inches: "))
# print(f"{inches} inches = {inches_to_cm(inches)} cm")

# def remove_and_strip(word_list, word_to_remove):
#     cleaned_list = []
#     for item in word_list:
#         item = item.strip()       # remove spaces
#         if item != word_to_remove:  # skip the given word
#             cleaned_list.append(item)
#     return cleaned_list

# words = ["  apple  ", "banana", "  mango  ", "banana  "]
# result = remove_and_strip(words, "banana")
# print(result)

# def table(n):
#     print(f"table of {n}:")
#     for i in range(1,11):
#         print(f"{n} x {i} = {n*i}")
# print(table(2))        