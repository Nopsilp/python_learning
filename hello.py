original_list = [1, 2, 3, 4, 5]
print(id(original_list))

original_list[:]
print(id(original_list[:]))

sliced_list = original_list[1:4]
print(id(sliced_list))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(id(numbers))

numbers[2:5] = [13, 14, 15]  # Modifying a portion of the list
print(id(numbers))
