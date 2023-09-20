import random

def generate_random_number():
    try:
        min_range = int(input("Enter the minimum number: "))
        max_range = int(input("Enter the maximum number: "))
        if min_range >= max_range:
            print("Invalid range. The minimum number should be less than the maximum number.")
            return

        random_number = random.randint(min_range, max_range)
        print(f"Random number between {min_range} and {max_range}: {random_number}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    print("Random Number Generator")
    generate_random_number()
