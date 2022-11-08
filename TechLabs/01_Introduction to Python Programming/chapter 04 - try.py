'''1. Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except
and put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below.'''

# # MY TRIAL
#
# int_list = []
# user_int = int(input("Choose how many integers you want to give: "))
#
# for i in range(0, user_int):
#     user_int = int(input("Enter a number: "))
#
#     int_list.append(user_int)
#
# print(f"Here's your list: {int_list}")
#
#
# largest_so_far = -1
# for num in int_list:
#     if num > largest_so_far:
#         largest_so_far = num
# print(f"The largest integer is: {largest_so_far}")
#
#
#
# smallest = None
# for num in int_list:
#     if smallest is None:
#         smallest = num
#     elif num < smallest:
#         smallest = num
# print(f"The smallest integer is: {smallest}")



# CORRECT ANSWER

largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        num = int(num)
    except:
        if num == "done": break
        else:
            print("Invalid input, please enter a number.")
            continue
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num
print("Maximum is", largest)
print("Minimum is", smallest)