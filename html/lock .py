def print_grid(pattern_points=None):
    size = 9
    pattern_points = pattern_points or []
    
    for row in range(size):
        line = ""
        for col in range(size):
            point_num = row * size + col + 1
            if point_num in pattern_points:
                line += " X "
            else:
                # Print point number, padded for alignment
                line += f"{point_num:2d} "
        print(line)
    print()

def main():
    print("9x9 Screen Lock Pattern Grid")
    print("Points are numbered 1 to 81 from left to right, top to bottom.")
    print("Example: Top-left point is 1, bottom-right is 81.")
    print_grid()
    
    user_input = input("Enter your pattern as point numbers separated by spaces (e.g. 1 10 19 28): ")
    try:
        pattern_points = list(map(int, user_input.strip().split()))
        
        # Validate points are in range and no duplicates
        if any(p < 1 or p > 81 for p in pattern_points):
            print("Error: Points must be between 1 and 81.")
            return
        if len(pattern_points) != len(set(pattern_points)):
            print("Error: Duplicate points detected in pattern.")
            return
        
        print("\nYour pattern on the 9x9 grid:")
        print_grid(pattern_points)
        
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")

if __name__ == "__main__":
    main()