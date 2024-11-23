try: 
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    if length == width:
        exit("This tool does not calculate area of squares")
    else:
        area = length*width
        print(area)

except ValueError:
    print("Please enter a number.")