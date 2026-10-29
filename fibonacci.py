def fibonacci_iterative(n: int) -> int:
    if n <= 1:
        raise ValueError("n must be greater than 1.")
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if n == 0:
        return 0
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


if __name__ == "__main__":
    # Example: first 7 terms
    print(fibonacci_iterative(4))  # Output: [0, 1, 1, 2, 3, 5, 8]
