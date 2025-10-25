# tests/test_operations.py

"""
Unit tests for the operations module using pytest.

This test suite covers both positive and negative scenarios for the Operation
class's static methods. It ensures that arithmetic operations perform correctly
and handle edge cases appropriately.

Tests are organized following the AAA (Arrange, Act, Assert) pattern and adhere
to PEP8 standards for code style and formatting.
"""

import pytest
from app.operations import Operations


# -----------------------------------------------------------------------------------
# Test Addition Method
# -----------------------------------------------------------------------------------

def test_addition_positive():
    """
    Test the addition method with two positive numbers.
    
    This test verifies that adding two positive numbers returns the correct sum.
    """
    # Arrange
    a = 9.0
    b = 5.0
    expected_result = 14.0

    # Act
    result = Operations.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


def test_addition_negative_numbers():
    """
    Test the addition method with two negative numbers.
    
    This test verifies that adding two negative numbers returns the correct sum.
    """
    # Arrange
    a = -8.0
    b = -2.0
    expected_result = -10.0

    # Act
    result = Operations.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


def test_addition_positive_negative():
    """
    Test the addition method with one positive and one negative number.
    
    This test verifies that adding a positive and a negative number returns the correct sum.
    """
    # Arrange
    a = 4.0
    b = -2.0
    expected_result = 2.0

    # Act
    result = Operations.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + ({b}) to be {expected_result}, got {result}"


def test_addition_with_zero():
    """
    Test the addition method with zero as one of the operands.
    
    This test verifies that adding zero to a number returns the number itself.
    """
    # Arrange
    a = 5.0
    b = 0.0
    expected_result = 5.0

    # Act
    result = Operations.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Subtraction Method
# -----------------------------------------------------------------------------------

def test_subtraction_positive():
    """
    Test the subtraction method with two positive numbers.
    
    This test verifies that subtracting two positive numbers returns the correct difference.
    """
    # Arrange
    a = 5.0
    b = 3.0
    expected_result = 2.0

    # Act
    result = Operations.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, got {result}"


def test_subtraction_negative_numbers():
    """
    Test the subtraction method with two negative numbers.
    
    This test verifies that subtracting two negative numbers returns the correct difference.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = -5.0

    # Act
    result = Operations.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - ({b}) to be {expected_result}, got {result}"


def test_subtraction_positive_negative():
    """
    Test the subtraction method with one positive and one negative number.
    
    This test verifies that subtracting a negative number from a positive number returns the correct difference.
    """
    # Arrange
    a = 13.0
    b = -2.0
    expected_result = 15.0

    # Act
    result = Operations.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - ({b}) to be {expected_result}, got {result}"


def test_subtraction_with_zero():
    """
    Test the subtraction method with zero as one of the operands.
    
    This test verifies that subtracting zero from a number returns the number itself.
    """
    # Arrange
    a = 4.0
    b = 0.0
    expected_result = 4.0

    # Act
    result = Operations.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Multiplication Method
# -----------------------------------------------------------------------------------

def test_multiplication_positive():
    """
    Test the multiplication method with two positive numbers.
    
    This test verifies that multiplying two positive numbers returns the correct product.
    """
    # Arrange
    a = 5.0
    b = 5.0
    expected_result = 25.0

    # Act
    result = Operations.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


def test_multiplication_negative_numbers():
    """
    Test the multiplication method with two negative numbers.
    
    This test verifies that multiplying two negative numbers returns the correct product.
    """
    # Arrange
    a = -4.0
    b = -5.0
    expected_result = 20.0

    # Act
    result = Operations.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


def test_multiplication_positive_negative():
    """
    Test the multiplication method with one positive and one negative number.
    
    This test verifies that multiplying a positive number by a negative number returns the correct product.
    """
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = -50.0

    # Act
    result = Operations.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * ({b}) to be {expected_result}, got {result}"


def test_multiplication_with_zero():
    """
    Test the multiplication method with zero as one of the operands.
    
    This test verifies that multiplying any number by zero returns zero.
    """
    # Arrange
    a = 2.0
    b = 0.0
    expected_result = 0.0

    # Act
    result = Operations.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Division Method
# -----------------------------------------------------------------------------------

def test_division_positive():
    """
    Test the division method with two positive numbers.
    
    This test verifies that dividing two positive numbers returns the correct quotient.
    """
    # Arrange
    a = 4.0
    b = 2.0
    expected_result = 2.0

    # Act
    result = Operations.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


def test_division_negative_numbers():
    """
    Test the division method with two negative numbers.
    
    This test verifies that dividing two negative numbers returns the correct quotient.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = 2.0

    # Act
    result = Operations.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


def test_division_positive_negative():
    """
    Test the division method with one positive and one negative number.
    
    This test verifies that dividing a positive number by a negative number returns the correct quotient.
    """
    # Arrange
    a = 15.0
    b = -5.0
    expected_result = -3.0

    # Act
    result = Operations.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / ({b}) to be {expected_result}, got {result}"


def test_division_with_zero_divisor():
    """
    Test the division method with zero as the divisor.
    
    This test verifies that dividing any number by zero raises a ValueError.
    """
    # Arrange
    a = 10.0
    b = 0.0

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        Operations.division(a, b)
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Division by zero is not allowed."


def test_division_with_zero_numerator():
    """
    Test the division method with zero as the numerator.
    
    This test verifies that dividing zero by a non-zero number returns zero.
    """
    # Arrange
    a = 0.0
    b = 5.0
    expected_result = 0.0

    # Act
    result = Operations.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Power Method
# -----------------------------------------------------------------------------------

def test_power_positive():
    """
    Test the power method with two positive numbers.
    
    This test verifies that raising a to b power with two positive numbers returns 
    the correct product.
    """
    # Arrange
    a = 2.0
    b = 3.0
    expected_result = 8.0

    # Act
    result = Operations.power(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} ** {b} to be {expected_result}, got {result}"


def test_power_negative_numbers():
    """
    Test the multiplication method with two negative numbers.
    
    This test verifies that taking the power two negative numbers returns the correct product.
    """
    # Arrange
    a = -2.0
    b = -2.0
    expected_result = 0.25

    # Act
    result = Operations.power(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} ** {b} to be {expected_result}, got {result}"


def test_power_positive_negative():
    """
    Test the multiplication method with one positive and one negative number.
    
    This test verifies that multiplying a positive number by a negative number returns the correct product.
    """
    # Arrange
    a = 2.0
    b = -2.0
    expected_result = 0.25

    # Act
    result = Operations.power(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} ** ({b}) to be {expected_result}, got {result}"

def test_power_with_zeroa():
    """
    Test the power method with zero as operand a.
    
    This test verifies that raising zero to any power returns zero.
    """
    # Arrange
    a = 0.0
    b = 5.0
    expected_result = 0.0

    # Act
    result = Operations.power(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} ** {b} to be {expected_result}, got {result}"


def test_power_with_zerob():
    """
    Test the power method with zero as operand b.
    
    This test verifies that raising any number to zero power returns one.
    """
    # Arrange
    a = 5.0
    b = 0.0
    expected_result = 1.0

    # Act
    result = Operations.power(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} ** {b} to be {expected_result}, got {result}"

# -----------------------------------------------------------------------------------
# Test Root Method
# -----------------------------------------------------------------------------------

def test_root_positive():
    """
    Test the root method with two positive numbers.
    
    This test verifies that dividing two positive numbers returns the correct number.
    """
    # Arrange
    a = 4.0
    b = 2.0
    expected_result = 2.0

    # Act
    result = Operations.root(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} root {b} to be {expected_result}, got {result}"


def test_root_negative_numbers(): 
    """
    Test the division method with two negative numbers.
    
    This test verifies that finding the negative root of a negative number returns
    the correct exception message.
    """
    # Arrange
    a = -27.0
    b = -3.0

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        Operations.root(a, b)
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "'b'th root must be a positive number."


def test_root_negative_positive_odd():
    """
    Test the root method with negative a and positive odd 'b'th root.
    
    This test verifies that that the positive odd root of a negative 
    number returns the correct result.
    """
    # Arrange
    a = -27.0
    b = 3.0
    expected_result = -3.0

    # Act
    result = Operations.root(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} root ({b}) to be {expected_result}, got {result}"


def test_root_negative_positive_even():
    """
    Test the root method for an even 'b'th root of a negative a value .
    
    This test verifies taking an even root of negative number returns a ValueError.
    """
    # Arrange
    a = -4.0
    b = 2.0

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        Operations.root(a, b)
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Cannot take even root of a negative number."


def test_root_negative_with_decimal():
    """
    Test the root method with fractional 'b'th root.
    
    This test verifies that taking a fractional root of a negative number returns
    the correct exception message.
    """
    # Arrange
    a = -100.0
    b = 5.25

     # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        Operations.root(a, b)
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Cannot take fractional root of a negative number."

def test_zeroth_root():
    """
    Test the root method with zero-th root.
    
    This test verifies that taking a taking the zero root of a number returns
    the correct exception message.
    """
    # Arrange
    a = 4.0
    b = 0.0

     # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        Operations.root(a, b)
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "'0'th Root is undefined operation."


# -----------------------------------------------------------------------------------
# Test Modulus Method
# -----------------------------------------------------------------------------------

def test_modulus_positive():
    """
    Test the modulus method with two positive numbers.
    
    This test verifies that the modulus of two positive numbers returns the correct number.
    """
    # Arrange
    a = 5.0
    b = 2.0
    expected_result = 1.0

    # Act
    result = Operations.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, got {result}"


def test_modulus_negative_numbers():
    """
    Test the modulus method with two negative numbers.
    
    This test verifies that the modulus of two negative numbers returns the correct number.
    """
    # Arrange
    a = -5.0
    b = -2.0
    expected_result = -1.0

    # Act
    result = Operations.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, got {result}"


def test_modulus_positive_negative():
    """
    Test the modulus method with one positive and one negative number.
    
    This test verifies that the modulus of a positive dividend by a negative divisor returns the correct number.
    """
    # Arrange
    a = 5.0
    b = -2.0
    expected_result = -1.0

    # Act
    result = Operations.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % ({b}) to be {expected_result}, got {result}"

def test_modulus_negative_positive():
    """
    Test the modulus method with one positive and one negative number.
    
    This test verifies that the modulus of a negative dividend by a positive divisor returns the correct number.
    """
    # Arrange
    a = -5.0
    b = 2.0
    expected_result = 1.0

    # Act
    result = Operations.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % ({b}) to be {expected_result}, got {result}"

def test_modulus_with_zero_divisor():
    """
    Test the modulus method with zero as the divisor.
    
    This test verifies that dividing any number by zero raises a ValueError.
    """
    # Arrange
    a = 5.0
    b = 0.0

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        Operations.modulus(a, b)
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Division by zero is not allowed."


def test_modulus_with_zero_numerator():
    """
    Test the modulus method with zero as the dividend.
    
    This test verifies that dividing zero by a non-zero number returns zero.
    """
    # Arrange
    a = 0.0
    b = 5.0
    expected_result = 0.0

    # Act
    result = Operations.modulus(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} % {b} to be {expected_result}, got {result}"

# -----------------------------------------------------------------------------------
# Test Integer Division Method
# -----------------------------------------------------------------------------------

def test_intdivision_positive():
    """
    Test the intdivision method with two positive numbers.
    
    This test verifies that dividing two positive numbers returns the correct quotient.
    """
    # Arrange
    a = 10.0
    b = 3.0
    expected_result = 3.0

    # Act
    result = Operations.intdivision(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} // {b} to be {expected_result}, got {result}"


def test_intdivision_negative_numbers():
    """
    Test the intdivision method with two negative numbers.
    
    This test verifies that dividing two negative numbers returns the correct quotient.
    """
    # Arrange
    a = -10.0
    b = -3.0
    expected_result = 3.0

    # Act
    result = Operations.intdivision(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} // {b} to be {expected_result}, got {result}"


def test_intdivision_positive_negative():
    """
    Test the intdivision method with one positive and one negative number.
    
    This test verifies that dividing a positive number by a negative number returns the correct quotient.
    """
    # Arrange
    a = 10.0
    b = -3.0
    expected_result = -4.0

    # Act
    result = Operations.intdivision(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} // ({b}) to be {expected_result}, got {result}"


def test_intdivision_with_zero_divisor():
    """
    Test the intdivision method with zero as the divisor.
    
    This test verifies that dividing any number by zero raises a ValueError.
    """
    # Arrange
    a = 10.0
    b = 0.0

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        Operations.intdivision(a, b)
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Division by zero is not allowed."


def test_intdivision_with_zero_numerator():
    """
    Test the intdivision method with zero as the numerator.
    
    This test verifies that dividing zero by a non-zero number returns zero.
    """
    # Arrange
    a = 0.0
    b = 5.0
    expected_result = 0.0

    # Act
    result = Operations.intdivision(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} // {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Percentage Method
# -----------------------------------------------------------------------------------

def test_percentage_positive():
    """
    Test the percentage method with two positive numbers.
    
    This test verifies that taking the percentage two positive numbers returns the correct number.
    """
    # Arrange
    a = 5.0
    b = 20.0
    expected_result = 25.0

    # Act
    result = Operations.percentage(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} percent {b} to be {expected_result}, got {result}"


def test_percentage_negative_numbers():
    """
    Test the percentage method with two negative numbers.
    
    This test verifies that finding the percent two negative numbers returns the correct number.
    """
    # Arrange
    a = -5.0
    b = -20.0
    expected_result = 25.0

    # Act
    result = Operations.percentage(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} percent {b} to be {expected_result}, got {result}"


def test_percentage_positive_negative():
    """
    Test the percentage method with one positive and one negative number.
    
    This test verifies that finding the percent of a positive number by a negative number returns the correct number.
    """
    # Arrange
    a = 5.0
    b = -20.0
    expected_result = -25.0

    # Act
    result = Operations.percentage(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} percent ({b}) to be {expected_result}, got {result}"


def test_percentage_with_zero_divisor():
    """
    Test the percentage method with zero as the divisor, any percentage of zero.
    
    This test verifies that finding any percent of zero with return zero.
    """
    # Arrange
    a = 10.0
    b = 0.0
    expected_result = 0.0

    # Act & Assert
    result = Operations.percentage(a, b)
    
    # Verify that the exception message is as expected
    assert result == expected_result, f"Expected {a} percent ({b}) to be {expected_result}, got {result}"


def test_percentage_with_zero_numerator():
    """
    Test the percentage method with zero as the numerator.
    
    This test verifies that finding zero percent of a non-zero number returns zero.
    """
    # Arrange
    a = 0.0
    b = 5.0
    expected_result = 0.0

    # Act
    result = Operations.percentage(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} percent {b} to be {expected_result}, got {result}"

# -----------------------------------------------------------------------------------
# Test Absolute Differnce Method
# -----------------------------------------------------------------------------------

def test_absolute_differnce_positive():
    """
    Test the absolute differnce method with two positive numbers.
    
    This test verifies that subtracting two positive numbers returns the correct difference.
    """
    # Arrange
    a = 5.0
    b = 3.0
    expected_result = 2.0

    # Act
    result = Operations.absolute_difference(a, b)

    # Assert
    assert result == expected_result, f"Expected |{a} - {b}| to be {expected_result}, got {result}"


def test_absolute_difference_negative_numbers():
    """
    Test the absolute differnce method with two negative numbers.
    
    This test verifies that the absolute difference of two negative numbers returns the correct difference.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = 5.0

    # Act
    result = Operations.absolute_difference(a, b)

    # Assert
    assert result == expected_result, f"Expected |({a}) - ({b})| to be {expected_result}, got {result}"


def test_absolute_difference_positive_negative():
    """
    Test the absolute difference method with one positive and one negative number.
    
    This test verifies that subtracting a negative number from a positive number returns the 
    correct absolute difference.
    """
    # Arrange
    a = -3.0
    b = 12.0
    expected_result = 15.0

    # Act
    result = Operations.absolute_difference(a, b)

    # Assert
    assert result == expected_result, f"Expected |{a} - ({b})| to be {expected_result}, got {result}"


def test_absolute_difference_with_zero():
    """
    Test the absolute difference method with zero as one of the operands.
    
    This test verifies that subtracting zero from a number returns the number itself.
    """
    # Arrange
    a = 0.0
    b = 4.0
    expected_result = 4.0

    # Act
    result = Operations.absolute_difference(a, b)

    # Assert
    assert result == expected_result, f"Expected |{a} - {b}| to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Invalid Input Types (Negative Testing)
# -----------------------------------------------------------------------------------

@pytest.mark.parametrize("calc_method, a, b, expected_exception", [
    (Operations.addition, '10', 5.0, TypeError),
    (Operations.subtraction, 10.0, '5', TypeError),
    (Operations.multiplication, '10', '5', TypeError),
    (Operations.division, 10.0, '5', TypeError),
])
def test_operations_invalid_input_types(calc_method, a, b, expected_exception):
    """
    Test that arithmetic methods raise TypeError when provided with invalid input types.
    
    This test verifies that providing non-float inputs to the arithmetic methods raises
    a TypeError, as the operations are intended for floating-point numbers.
    """
    # Arrange
    # No setup needed as the invalid inputs are provided directly

    # Act & Assert
    with pytest.raises(expected_exception):
        calc_method(a, b)

