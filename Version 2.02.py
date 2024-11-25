def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    return sum(numbers)  # Assumes all inputs are valid without validation.

# Example usage:
nums = [1, 2, "3", 4, 5]  # Vulnerable to non-integer inputs.
print(f"Sum of {nums} is {calculate_sum(nums)}")  # Will raise a TypeError.
