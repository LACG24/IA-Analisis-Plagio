from Dynamic_class import MathOperations

# Test Cases
def run_checks():
    math_ops = MathOperations()
    assert math_ops.add(4, 5) == 9, "Test case failed: Incorrect addition result"
    assert math_ops.multiply(4, 5) == 20, "Test case failed: Incorrect multiplication result"

# Running test cases
run_checks()
print("Test cases passed for dynamic functions.")