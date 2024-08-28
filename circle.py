import math

r = 5

def get_area():
    # r = float(input("Radius: "))
    return math.pi * r ** 2.0

def get_circumference():
    # r = float(input("Radius: "))
    return 2.0 * math.pi * r
    
def main(): 
    area = get_area()
    circumference = get_circumference()
    print(area)
    print(circumference)


if __name__ == "__main__":
    main()