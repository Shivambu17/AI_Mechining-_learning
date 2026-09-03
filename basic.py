def CalcArea(length, width):
    
    area=length * width
    return area

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area=CalcArea(length, width)
print("The area of the rectangle is:", area)