'''******STRINGS******
Ques.1. Write a python program to display a user entered name followed by Good 
Afternoon using input () function. 
name = input("Enter the name:")
print("GoodAfternoon",name)

Ques 2. Write a program to fill in a letter template given below with name and date. 
letter =  
Dear <|Name|>, 
You are selected! 
<|Date|> 

letter = """Dear Aditya,
You are selected!
Date-19/10/2026"""
print(letter)

Ques 3. Write a program to detect double space in a string. 
text = input("Enter the text:")
if "  " in text:
    print("detect double space in stirng")
else:
     print("Not double space in string")    

 ques.4  Replace the double space from problem 3 with single spaces. 
 text = input("enter the text:")
 if "  " in text:
     new=text.replace("  "," ");
    print(new);

ques.5. Write a program to format the following letter using escape sequence 
characters. 
letter = "Dear Harry, this python course is nice. Thanks!"

letter="\n Dear Harry,\n This python course is nice.\n Thanks!"
print(letter)'''










