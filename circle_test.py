# import the Circle class from circle.py
from circle import Circle 

def main():
    # construct circle with radius 5
    circle = Circle (5) 
    
    # print the area of the circle
    print("The area of the circle is " + str(circle.get_area()))

    # print the circumference of the circle
    print("The circumference of the circle is " + str(circle.get_circumference()))
  
if __name__ == "__main__":
    main()