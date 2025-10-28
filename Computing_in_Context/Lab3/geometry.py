
# This program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.

import circle
import rectangles
import triangles
import spheres
import cylinders

# The main function.

def main():
    
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0

    while not(choice == 11):
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input("Enter your choice: "))

        # Perform the selected action.
        if choice == 1:
            radius = float(input("Enter the circle's radius: "))
            print(f"The area of the circle is {circle.area(radius):.3f}.")      
        elif choice == 2:
            radius = float(input("Enter the circle's radius: "))
            print(f"The circumference of the circle is {circle.circumference(radius):.3f}.")
        elif choice == 3:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print(f"The area of the rectangle is {rectangles.area(width,length):.3f}.")
        elif choice == 4:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print(f"The perimeter of the rectangle is {rectangles.perimeter(width,length):.3f}.")
        elif choice == 5:
            base = float(input("Enter the triangle's base: "))
            height = float(input("Enter the triangle's height: "))
            print(f"The area of the triangle is {triangles.area(base,height):.3f}.")
        elif choice == 6:
            side1 = float(input("Enter the triangle's first side: "))
            side2 = float(input("Enter the triangle's second side: "))
            side3 = float(input("Enter the triangle's third side: "))
            print(f"The perimeter of the triangle is {triangles.perimeter(side1,side2,side3):.3f}.")
        elif choice == 7:
            radius = float(input("Enter the sphere's radius: "))
            print(f"The volume of the sphere is {spheres.volume(radius):.3f}.")
        elif choice == 8:
            radius = float(input("Enter the sphere's radius: "))
            print(f"The surface area of the sphere is {spheres.surface(radius):.3f}.")
        elif choice == 9:
            radius = float(input("Enter the cylinder's radius: "))
            height = float(input("Enter the cylinder's height: "))
            print(f"The volume of the cylinder is {cylinders.volume(radius,height):.3f}.")
        elif choice == 10:
            radius = float(input("Enter the cylinder's radius: "))
            height = float(input("Enter the cylinder's height: "))
            print(f"The surface area of the cylinder is {cylinders.surface(radius,height):.3f}.")
        elif choice == 11:
            print("Exiting the program...")
        else:
            print("Error: invalid selection.")
    
# The display_menu function displays a menu.
def display_menu():
    print("        MENU for ")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Area of a triangle")
    print("6) Perimeter of a triangle")
    print("7) Volume of a sphere")
    print("8) Surface area of a sphere")
    print("9) Volume of a cylinder")
    print("10) Surface area of a cylinder")
    print("11) Quit")

# Call the main function.
main()