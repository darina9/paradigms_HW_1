# Императивный стиль
def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


my_numbers = [4, 2, 7, 1, 9, 3, 6]
sort_list_imperative(my_numbers)
print(my_numbers)
