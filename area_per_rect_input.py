#!/usr/bin/env python3
# Created By: Angelo Garcia
# Date: sept. 19, 2025
# This program calculates and displays the area and perimeter of a rectangle based on user input.


def main():
    # Get user input for length and width
    length = float(input("Enter the length of the rectangle (cm): "))
    width = float(input("Enter the width of the rectangle (cm): "))
    print()
    print(
        "For a rectangle with a length of {}cm and a width of {}cm:".format(
            length, width
        )
    )
    print()
    print("The area is: {}cm²".format(length * width))
    print("The perimeter is: {}cm".format(2 * (length + width)))


if __name__ == "__main__":
    main()
