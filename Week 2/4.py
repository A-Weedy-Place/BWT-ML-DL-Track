def find_max_min(numbers):
    max_value = numbers[0]
    min_value = numbers[0]
    for n in numbers:
        max_value = max(max_value, n)
        min_value = min(min_value, n)
    return max_value, min_value

numbers = []
for i in range(5):
  n = int(input(f"Enter number {i+1}: "))
  numbers.append(n)

max_value, min_value = find_max_min(numbers)

print(f"The maximum value is: {max_value}")
print(f"The minimum value is: {min_value}")