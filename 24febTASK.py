def CheckIndexIsFilled(index, val):
    if list_1[index] is not None:
        print("This key is already filled.")
    else:
        list_1.insert(index, val)
        print("Value added successfully.")


def lifo_list(new_val, list_2):
    list_2.insert(0, new_val)
    if len(list_2) > 5:
        list_2.pop()
    return list_2


def duplicate(value, list_3):
    if value in list_3:
        print(f"Value '{value}' is already in the list.")
    else:
        list_3.append(value)
        print(list_3)


def multi_dim(rows,cols):
    # Create an empty multi-dimensional array with the specified size
    multi_array = [[None] * cols for i in range(rows)]

    # Loop through each element in the multi-dimensional array and get the value from the user
    for i in range(rows):
        for j in range(cols):
            multi_array[i][j] = input("Enter the value for element at row " + str(i) + " and column " + str(j) + ": ")

    # Print the multi-dimensional array
    print("Multi-dimensional array:")
    for i in range(rows):
        for j in range(cols):
            print(multi_array[i][j], end="\t")
        print()

# ........................................First..Problem.............................................
# write a method with take key, value from the user and add that value in the list..
# ... if key is already filled should return message to user to chose another key. length of list will be 10


list_1 = [14, 69, 1, 98, 8, 9, 41, 5, 77]
index = int(input('Enter the index, Where you want to Insert the Val:'))
val = int(input('Enter the Value, Which you want to Insert in the List:'))
# using the method created above
CheckIndexIsFilled(index, val)


# ........................................Second..Problem.............................................
# write a method with fixed length of list 5. if user enter more ....
# ...then 5th value in the list bottom value should be removed and new value should be added at the top of list


# fetching five vals from the list1
list_2 = list_1[:5]

new_val = int(input("Enter the new val to be added:"))
# using the method created above
print(lifo_list(new_val, list_2))


# ........................................Third..Problem.............................................
# write a method with list of random numbers, when user add new value methode will check if the value ..
# already exist in list return message "value already in the list otherwise add the value in the list and ..
# display back the list till that value


list_3 = [14, 69, 1, 98, 8, 9, 41, 5, 77] # a random list
value = int(input('enter value to be added , Duplicate Check:'))
# using the method created above
duplicate(value, list_3)

# ........................................Fourth..Problem.............................................

# Define the size of the multi-dimensional array
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
# using the method created above
multi_dim(rows,cols)
