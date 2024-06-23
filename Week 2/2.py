def is_even(num):
    num = num % 2
    if (num == 0):
        return True
    else:
        return False

number = int (input("Enter the number: "))
if is_even(number):
  print(f"{number} is even")
else:
  print(f"{number} is odd")
