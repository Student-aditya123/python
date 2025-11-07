'''*******Dictionary and Sets*******'''
# ques 1.Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up!
# hindi_dict = {
#         "pustak" : "book",
#          "kalam" : "pen",
#          "kutta" : "dog",
#          "billi" : "cat",
#          "kaan" : "ear",
#          "aankh" : "eye"
# }
# text = input("Enter the Hindi word to look up: ")
# if text in hindi_dict:
#     print("The english meaning is:",hindi_dict[text])
# else:
#     print("Sorry,The word is not found in dictionary")  
  
# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 
# s=set()
# for i in range(1,9):
#     num=int(input(f"Enter the number {i}: "))
#     s.add(num)
# print("unique numbers are",s)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it? 
# s={18,'18'}
# print(s) 

# 4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 
# print(s)
# print(len(s))

# 5. s = {} 
# What is the type of 's'? 
# s={}
# print(type(s))

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique

# <<<<<<<dictionary comprehensive>>>>>>
# my_dict = {input("enter your name:"):input("enter your favorite language: ") for i in range(1,5)}
# print(my_dict)
# print("enter your names and favorite language: ")
# for i in range(1, 5):
#      key = input("Enter you name:")
#      value= input("Enter your favorite language:")
#      my_dict[key]=value
# print(my_dict)    

#  If the names of 2 friends are same; what will happen to the program in problem 
# 6?
# Answer: suppose: firstly entered: name Aditya and language:Hindi
#               second entered: name: Aditya and language:English
# then in dectionary stored second value not first value.

# . If languages of two friends are same; what will happen to the program in problem 
# 6? 
# Answer: then there is no change as it is stored in the dictionary

# . Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 
# print(s)
# TypeError: cannot use 'list' as a set element (unhashable type: 'list')
