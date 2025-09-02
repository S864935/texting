f = open("demofile.txt")
print(f.read())
def number_changer(initial_number):
    """
    Performs a sequence of arithmetic operations on a number.

    Args:
        initial_number (int or float): The starting number.

    Returns:
        float: The final number after all operations.
    """
    print(f"Starting with the number: {initial_number}")

    # Operation 1: Add 10 to the number
    added_number = initial_number + 10
    print(f"After adding 10: {added_number}")

    # Operation 2: Multiply the result by 2
    multiplied_number = added_number * 2
    print(f"After multiplying by 2: {multiplied_number}")

    # Operation 3: Subtract 5 from the new number
    subtracted_number = multiplied_number - 5
    print(f"After subtracting 5: {subtracted_number}")

    # Operation 4: Divide the final number by 3
    divided_number = subtracted_number / 3
    print(f"After dividing by 3: {divided_number}")
    
    return divided_number

# ---
# Main Program Execution
# ---

if __name__ == "__main__":
    # You can change the starting number here to see how the result changes.
    starting_value = 15
    final_result = number_changer(starting_value)

    print("\n---")
    print(f"The final number is: {final_result}")
