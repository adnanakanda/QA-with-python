import time
import pytest

def test_prime_number():
    """Test to check if a number is prime."""
    number = 29
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    time.sleep(2)  # Simulate a test that takes time to run
    assert is_prime, f"{number} should be a prime number"

def test_palindrome():
    """Test to check if a string is a palindrome."""
    text = "radar"
    time.sleep(2)  # Simulate a test that takes time to run
    assert text == text[::-1], f"{text} should be a palindrome"


# use this command "pytest -n 2 Parallel_prac.py" from the folder directory to run the test in parallel
