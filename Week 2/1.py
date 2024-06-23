data = {}
data["name"] = input("Enter your name: ")
data["age"] = int(input("Enter your age: "))
while True:
    data["email"] = input("Enter your email: ")
    if "@" in data["email"] and "." in data["email"]:
      break
    else:
      print("Enter a valid email (abc@idk.com)")
data["favorite_number"] = int(input("Enter your favorite number: "))
print(f"Hello {data['name']}, you are {data['age']} years old, your email is {data['email']}, and your favorite number is {data['favorite_number']}.")