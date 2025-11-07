#  ****Modules,Comments and Pip**** 

#ques.1 Write a program to print Twinkle twinkle little star poem in python.

# print("Twinkle twinkle little star,");
# print("How I Wonder How you are!");
# print("up above the world so high,");
# print("Like a diamond in the sky.");
# print("Twinkle twinkle little star,");
# print("How I Wonder How you are!");

#Ques.2 print the table for n numbers. 

# n = int(input("Enter the number: "));
# for i in range(1 , n+1):
#  print(f"table of {i}:");
#  for j in range(1, 11):
#     print(f"{i} X {j} = {i*j}");

#Ques.3 Install an external module and use it to perform an operation of your interest. 

# import requests

# # Example: Get a random joke from an API
# response = requests.get("https://official-joke-api.appspot.com/random_joke")

# # Check if request was successful
# if response.status_code == 200:
#     data = response.json()
#     print("Here's a random joke:")
#     print(f"{data['setup']} - {data['punchline']}")
# else:
#     print("Failed to fetch joke.")

# import requests

# response = requests.get("https://api.github.com")
# print("Status code:", response.status_code)
# print("Response headers:")
# print(response.headers)
