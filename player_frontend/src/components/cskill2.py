# vacuum.py

# Get the dirt status of each square from the user
square_A = int(input("Enter the dirt status for each square (1 for Dirty, 0 for Clean):\nSquare A: "))
square_B = int(input("Square B: "))

# Vacuum starts at Square A
print("\nVacuum is at square A")

# Check and clean Square A if dirty
if square_A == 1:
    print("Cleaning square A...")
    square_A = 0

# Check and clean Square B if dirty
if square_B == 1:
    print("Moving to square B")
    print("Cleaning square B...")
    square_B = 0

# Final message when all squares are clean
if square_A == 0 and square_B == 0:
    print("\nAll squares are clean!")
    print("Vedant Tayade")