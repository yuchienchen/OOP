import math

r = 5

class Circle:
    def __init__(self, area, circumference):
        self.area = area
        self.circumference = circumference
    
    def __str__(self):
        return f"{self.area} is twice of {self.circumference}"
    
    @classmethod
    def get(cls):
        area = math.pi * r ** 2.0
        circumference = 2.0 * math.pi * r
        return cls(area, circumference)
        

# def get_area():
#     # r = float(input("Radius: "))
#     return math.pi * r ** 2.0

# def get_circumference():
#     # r = float(input("Radius: "))
#     return 2.0 * math.pi * r

    
def main(): 
    circle = Circle.get()
    # area = get_area()
    # circumference = get_circumference()
    # print(circle.area)
    # print(circle.circumference)
    print(circle)


if __name__ == "__main__":
    main()