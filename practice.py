
"""
marks = []

for i in range(5):
    marks.append(int(input(f"Enter the marks of Subject {i+1} : ")))

total = 0
for j in marks:
    total += j

average = total/(len(marks))

if average >= 90:
    print(f"A+:{average}")
elif average >= 80 and average < 90:
    print(f"B:{average}")
elif average >= 70 and average < 80:
    print(f"C:{average}")
elif average >= 60 and average < 70:
    print(f"D:{average}")
elif average < 60:
    print(f"F:{average}")
"""
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
"""
#Challenge 4: List Analysis
numbers = [12, 7, 23, 8, 15, 31, 4, 19]
#Count how many numbers are even vs odd
even_num_count = 0
odd_num_count = 0
largest_number = numbers[0]
smallest_number = numbers[0]
sum_of_numbers_gt_ten = 0

for index, item in enumerate(numbers):
    if (item % 2) == 0:
        even_num_count += 1
    else:
        odd_num_count += 1
    
    if(index > 0):
        if item > largest_number:
            largest_number = item
        elif item < smallest_number:
            smallest_number = item

    if(item > 10):
        sum_of_numbers_gt_ten += item 

print(f"a. Even numbers count in the list is {even_num_count} & Odd number count in the list is {odd_num_count}")
print(f"b. Largest number in the list is {largest_number} & smallest number in the list is {smallest_number}")
print(f"c. Sum of numbers greater than 10 in the list is {sum_of_numbers_gt_ten}")

#############################
"""
Challenge 1: Temperature Converter
Write a function that converts Celsius to Fahrenheit using: F = (C × 9/5) + 32
"""
#############################

def celsius_to_farenheit(celsius):
    return ((celsius * (9/5)) + 32)

print(celsius_to_farenheit(5))

#############################
"""
Challenge 2: List Analyzer
Write a function that takes a list of numbers and returns both the maximum and minimum values.
"""
#############################


def get_max_min_in_lists(list_name):
    for index,item in enumerate(list_name):
        if index == 0:
            max_value = item
            min_value = item
        else:
            if item > max_value:
                max_value = item
        
            if item < min_value:
                min_value = item
    
    return max_value,min_value

numbers = [12, 7, 23, 8, 15, 31, 4, 19]
max_num , min_num = get_max_min_in_lists(numbers)
print(f"Max number is {max_num} & Min number is {min_num}")

#############################
"""
Challenge 3: Grade Converter
Write a function that takes a numerical grade (0-100) and returns the corresponding letter grade.
"""
#############################

def grade_converter(marks):

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    elif marks < 60:
        grade = "F"    
    return grade

print(grade_converter(95))  # Should print "A"
print(grade_converter(82))  # Should print "B"
print(grade_converter(67))  # Should print "D"
print(grade_converter(45))  # Should print "F"