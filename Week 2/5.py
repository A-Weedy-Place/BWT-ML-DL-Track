def get_student_info():
  students = {}
  for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    age = int(input("Enter age: "))
    grade = float(input("Enter grade: "))
    students[name] = (age, grade)
  return students

student_dict = get_student_info()

for name, info in student_dict.items():
    age, grade = info
    print(f"\nStudent: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")