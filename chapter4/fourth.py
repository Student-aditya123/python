'''*******Lists and Tuples*******
ques1. Write a program to store seven fruits in a list entered by the user.
list = []
for i in range(1, 8):
    fruit = input("Enter the fruits name:");
    list.append(fruit)
print(list)  

ques.2 Write a program to accept marks of 6 students and display them in a sorted 
manner
list = []
for i in range(1, 7):
    num = int(input("Enter the marks of student: "))
    list.append(num)
list.sort()
print(list)  

ques3. Check that a tuple type cannot be changed in python.
tuple = (1,2,3,4,5,6)
print(tuple)
tuple[0]=9   TypeError: 'tuple' object does not support item assignment
print(tuple)

ques4. Write a program to sum a list with 4 numbers.
new_list=[]   
list1 = [1,2,3,4,5] #(not used name "list")
for i in list1:
     new = i + 4 #(not used like this list[i] ,beco'z here i is an element not index)
     new_list.append(new)
print(new_list)    
 
ques5.Write a program to count the number of zeros in the following tuple: 
a = (7, 0, 8, 0, 0, 9)
a=(7,0,8,0,0,9)
print(f"the number of zeros present in tuple:",a.count(0))'''
 