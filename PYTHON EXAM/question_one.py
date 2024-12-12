#i)
def area_of_a_circle():
    radius = int(input("Enter the radius of the circle:"))
    pie = 3.14
    area = pie*radius**2
    print(f'The area of the circle with radius{radius} is {area:.3f}')
area_of_a_circle()    



#ii)
numbers = [4, 7, 2, 9, 12, 15]
sum_of_odds = 0
for num in numbers:
    if num % 2 != 0:
        sum_of_odds += num
print("Sum of odd numbers:", sum_of_odds)


#iii)
def arithmetic_operations(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2

    if num2 != 0:
        quotient_result = num1 / num2
    else:
        quotient_result = "Undefined (division by zero)"
    
    return sum_result, difference_result, product_result, quotient_result

num1 = 10
num2 = 5
results = arithmetic_operations(num1, num2)
print("Sum:", results[0])
print("Difference:", results[1])
print("Product:", results[2])
print("Quotient:", results[3])


#v)
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}
student_info['age'] = 26
student_info['city'] = 'Kampala'
print(student_info)
