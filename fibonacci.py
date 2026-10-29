def fibonacci_iterative(n):
  a, b = 0, 1
  result = []
  for _ in range(n):
    result.append(a)
    a, b = b, a + b
  return result


if __name__ == "__main__":
    # Example: first 7 terms
    print(fibonacci_iterative(4))  # Output: [0, 1, 1, 2, 3, 5, 8]
