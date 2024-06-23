def convert_temperature(temp, scale):
    if scale == "C":
        temp = (temp * 9/5) + 32
        scale = "F"
        return temp, scale
    elif scale == "F":
        temp = (temp - 32) * 5/9
        scale = "C"
        return temp, scale
    else:
        print("Invalid scale. Enter 'C' or 'F'.")
        convert_temperature(temp, scale)
    
scale = input("Enter the scale: ")
temp = int (input("Enter the temperature: "))

temp1, scale1 = convert_temperature(temp, scale)

print(f"{temp:.2f} degrees {scale} is converted to {temp1:.2f} degrees {scale1}.")
