#i)
student_name = input("Enter student name: ")  
student_number = input("Enter student number: ")  
programming_marks = float(input("Enter marks for Programming: "))  
data_science_marks = float(input("Enter marks for Data Science: "))  
computer_apps_marks = float(input("Enter marks for Computer Applications: "))  
average_marks = (programming_marks + data_science_marks + computer_apps_marks) / 3
print("\nStudent Details:")
print(f"Student Name: {student_name}")
print(f"Student Number: {student_number}")
print(f"Programming Marks: {programming_marks}")
print(f"Data Science Marks: {data_science_marks}")
print(f"Computer Applications Marks: {computer_apps_marks}")
print(f"Average Marks: {average_marks:.3f}")  


#ii)
miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the number of gallons of gas used: "))
if gallons_used == 0:
    print("Error: Gallons of gas used cannot be zero.")
else:
    MPG = miles_driven / gallons_used
    print(f"The car's miles per gallon (MPG) is: {MPG:.2f}")
    
    
#iii)
def odd_numbers():
    for numbers in range(1,100,2):
        print(numbers)
odd_numbers()           