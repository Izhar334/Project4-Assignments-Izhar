#Index Game Solution

def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."

def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_element(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst, start, end))
    else:
        print("Invalid operation.")

index_game()

# This code defines a simple index game where the user can access, modify, or slice a list.
# It handles index errors gracefully and provides feedback to the user.
# The game is interactive and allows the user to choose the operation they want to perform on the list.
# The list is initialized with some example values, and the user can input their choices.
# The functions are modular and can be reused or extended for more complex operations in the future.
# The code is designed to be user-friendly and provides clear instructions for the user to follow.
# The game can be further enhanced by adding more operations or features, such as searching for elements or sorting the list.
# The current implementation is a good starting point for an index game and can be improved based on user feedback and requirements.

#List Practice Solution
# Create a list called fruit_list that contains the following fruits: 'apple', 'banana', 'orange', 'grape', 'pineapple'.
fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']

# Print the length of the list.
lst_length = len(fruit_lst)
print(lst_length)

# Add 'mango' at the end of the list. 
fruit_lst.append('mango')

# Print the updated list.
for fruit in fruit_lst:
    print(fruit)