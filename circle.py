import math

r = 5

class Circle:
    ...

# def get_area():
#     # r = float(input("Radius: "))
#     return math.pi * r ** 2.0

# def get_circumference():
#     # r = float(input("Radius: "))
#     return 2.0 * math.pi * r

def get_circle():
    circle = Circle()
    circle.area = math.pi * r ** 2.0
    circle.circumference = 2.0 * math.pi * r
    return circle
    
def main(): 
    circle = get_circle()
    # area = get_area()
    # circumference = get_circumference()
    print(circle.area)
    print(circle.circumference)


if __name__ == "__main__":
    main()