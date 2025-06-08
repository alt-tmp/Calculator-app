# Function to solve Tower of Hanoi
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    # Move nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)

# Input number of disks
if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))
    
    # A, B, C are names of rods
    tower_of_hanoi(n, 'A', 'C', 'B')

    print("Vedant")