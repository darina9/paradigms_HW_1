# Декларативный стиль

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


my_numbers = [4, 2, 7, 1, 9, 3, 6]
sorted_numbers = sort_list_declarative(my_numbers)
print(sorted_numbers)
