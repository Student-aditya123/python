# <<<<<<<<<< CHAPTER 9 – FILE I/O >>>>>>>>>>
# 1. Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 
# with open("poems.txt", "r") as f:  
#     text = f.read()
# # print(text)    
# if "twinkle" in text.lower():
#     print("Yes")
# else:
#     print("No")    
# 2. The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score.

# open("Hi-score.txt", "a").close()  

# def game():
#     score = int(input("Enter your score: "))
#     return score
# with open("Hi-score.txt", "r") as f1:
#       hiscore = f1.read()

# if hiscore == "":
#        hiscore = 0
# else:
#        hiscore = int(hiscore)            

# score = game()

# if score > hiscore:
#        with open("Hi-score-txt", "w") as f3:
#                f3.write(str(score))
#        print(f"New High Score! {score}")           
# else:
#         print(f"Your score: {score} | High score: {hiscore}")        

# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old. 

# for i in range(2, 21):
#     filename = f"table of {i}.txt"
#     with open("filename", "w") as f:
#         for j in range(1, 11):
#           f.write((f"{i} X {j} = {i * j}\n"))
# print("✅ All multiplication tables from 2 to 20 have been created!")

# 4. A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.  
# with open("filename","r") as f:
#     content = f.read();
# content = content.replace("Donkey", "####")
# with open("filename", "w") as f:
#      f.write(content) 
# print("update Successfuly!") 

# 5. Repeat program 4 for a list of such words to be censored. 
# word_to_censors = ["Donkey","stupid", "bad"]
# with open("filename", "r") as f:
#     content = f.read()
# for word in word_to_censors:
#     content = content.replace(word, "####")
# with open("filename", "w") as f:
#     f.write(content)    
# print("file update successfully!")

# 6. Write a program to mine a log file and find out whether it contains ‘python’. 
# with open("logfile.txt", "r") as f:
#     content = f.read()
# if "python" in content.lower():
#     print("yes contains python")
# else:
#     print("No found python")    

# 7. Write a program to find out the line number where python is present from ques 6.
# open("filename.txt", "a").close()
# with open("filename.txt", "r") as f:
#      for line_number, line in enumerate(f, start=1):
#            if "python" in line.lower():
#                  print(f"python found on line {line_number},{line.strip()}")

# 8. Write a program to make a copy of a text file “this. txt” 
# with open("filename.txt","r") as f:
#     content = f.read()
# with open("copy_filename.txt", "w") as f:
#         f.write(content)
# print("copied successfully!")        

# 9. Write a program to find out whether a file is identical & matches the content of 
# another file. 
# with open("filename.txt", "r") as f:
#      content1 = f.read()
# with open("copy_filename.txt", "r") as f:
#      content2 = f.readline()
# if content1 == content2:
#      print("yes")
# else:
#      print("No")     

# 💡 If you want to compare line-by-line instead::
# with open("filename.txt", "r") as f1, open("copy_filename.txt", "r") as f2:
#     for line_num, (l1, l2) in enumerate(zip(f1, f2), start=1):
#         if l1 != l2:
#             print(f"❌ Difference found on line {line_num}")
#             break
#     else:
#         print("✅ Both files are identical line by line.")

# ====>> zip(f1, f2)	Combines one line from each file
# ====>> enumerate(..., start=1)  Adds line numbers starting at 1

# 10. Write a program to wipe out the content of a file using python. 
# with open("filename.txt", "w") as f:
#     f.write("")

# 11. Write a python program to rename a file to “renamed_by_ python.txt. 
# import os
# old_name = "filename.txt"
# new_name = "newfilename.txt"
# os.rename(old_name, new_name)
# print("file rename from {old_name} to {new_name} successfully!")

# Why os is important

# Python alone can read/write files, but renaming, deleting, or moving files is done via os.

# It makes your programs cross-platform compatible (Windows, Linux, macOS).

# Many file-system related operations cannot be done without it.