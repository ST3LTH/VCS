def calculate_sum(numbers: list[int]) -> int:
    """Calculate the sum of a list of numbers."""
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")

    return sum(numbers)

# Example usage:
nums = [1, 2, 3, 4, 5]
print(f"Sum of {nums} is {calculate_sum(nums)}")
