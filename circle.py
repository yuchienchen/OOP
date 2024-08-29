import math

r = 5

class Circle:
    def __init__(self, area, circumference):
        self.area = area
        self.circumference = circumference

# def get_area():
#     # r = float(input("Radius: "))
#     return math.pi * r ** 2.0

# def get_circumference():
#     # r = float(input("Radius: "))
#     return 2.0 * math.pi * r

def get_circle():
    area = math.pi * r ** 2.0
    circumference = 2.0 * math.pi * r
    return Circle(area, circumference)    # constructor call
    
def main(): 
    circle = get_circle()
    # area = get_area()
    # circumference = get_circumference()
    print(circle.area)
    print(circle.circumference)


if __name__ == "__main__":
    main()