# This file is now called "Operations.py", and it contains a class `Operations` with four static methods:
# addition, subtraction, multiplication, and division.
# These methods are encapsulated within the `Operations` class, providing a structured way to perform basic math on two numbers.
# When we need to add, subtract, multiply, or divide numbers, we can call these static methods through the class.

class Operations:
    """
    The Operations class serves as a container for basic math operations.
    By using static methods, we can perform these operations without needing to create an instance of the class.
    """

    @staticmethod
    def addition(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their sum (a + b).
        The 'float' in the parentheses indicates that both 'a' and 'b' should be numbers with decimal points.
        The '-> float' part means that this method will return a number with decimals (a float) as the result.
        Example: if we call Operations.addition(5.0, 3.0), it will return 8.0.
        """
        return a + b  # This performs the addition of the two numbers and returns the result.

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their difference (a - b).
        Just like the addition method, it expects two numbers and returns their result.
        Example: if we call Operations.subtraction(10.0, 4.0), it will return 6.0.
        """
        return a - b  # This subtracts the second number (b) from the first number (a) and returns the result.

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their product (a * b).
        Multiplying means we take one number and increase it by the other number’s value repeatedly.
        Example: if we call Operations.multiplication(2.0, 3.0), it will return 6.0.
        """
        return a * b  # This multiplies the two numbers and returns the result.

    @staticmethod
    def division(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their quotient (a / b).
        Dividing means breaking the first number into equal parts based on the second number.
        BUT WAIT! There's an important check here: before we divide, we need to make sure that 'b' is not zero.
        
        Why? Because dividing by zero doesn't work. If we try to divide by zero, we get a big error!
        
        So, if 'b' is zero, we raise a 'ValueError', which is a way of telling the program, "Stop! You can't do this."
        Example: if we call Operations.division(10.0, 2.0), it will return 5.0.
        But if we call Operations.division(10.0, 0.0), it will raise a ValueError and say "Division by zero is not allowed."
        """
        if b == 0:
            # This part checks if 'b' is zero. If it is, we raise an error and stop the method.
            raise ValueError("Division by zero is not allowed.")  # This sends an error message when someone tries to divide by zero.
        return a / b  # If 'b' is not zero, we divide the first number (a) by the second number (b) and return the result.
    
    @staticmethod
    def power(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their power (a ** b).
        Power means we take one number (a) and multiply it by itself (b) times.
        Example: if we call Operations.power(2.0, 3.0), it will return 8.0.
        """
        return a ** b  # This multiplies the two numbers and returns the result.
    
    @staticmethod
    def root(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns the 'b' root of 'a'
        Root means a number multiplied that when by itself 'b' times gives 'a'
        Example: if we call Operations.root(4.0, 2.0), it will return 2.0.
        """
        if b == 0:
            raise ValueError("'0'th Root is undefined operation.") #0th root returns undefined value
        
        if b < 0:
            raise ValueError("'b'th root must be a positive number.") #nth root value must be positive

        if a < 0: #if a is negative number
            if float(b).is_integer(): #check if b is a whole number
                b_int = int(b) #convert b to int if value is a whole number
                
                if b_int % 2 == 0: #check if b is even
                    raise ValueError("Cannot take even root of a negative number.") #cant take even root of a negative number
                
                else: #b is odd
                    return -((-a) ** (1/b_int)) #b int root of int root of negative a number
            else:
                raise ValueError("Cannot take fractional root of a negative number.") #cant take root fractional root of a negative number

                

        return (a) ** (1/b)  # This returns the root the two numbers and returns the result.   

    @staticmethod
    def modulus(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns the remainder of this division operation.

        this method also checks if 'b' is zero and returns an exception message if this is the case
        Example: if we call Operations.modulus(10.0, 3.0), it will return 1.0.
        But if we call Operations.modulus(10.0, 0.0), it will raise a ValueError and say "Division by zero is not allowed."
        """
        if b == 0:
            # This part checks if 'b' is zero. If it is, we raise an error and stop the method.
            raise ValueError("Division by zero is not allowed.")  # This sends an error message when someone tries to divide by zero.
        return a % b  # If 'b' is not zero, we divide the first number (a) by the second number (b) and return the remainder.

    @staticmethod
    def intdivision(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their whole quotient, 
        discarding fractional part.
        """

        if b == 0:
            # This part checks if 'b' is zero. If it is, we raise an error and stop the method.
            raise ValueError("Division by zero is not allowed.")  # This sends an error message when someone tries to divide by zero.
        return a // b  #perform operation if b is not zero and return whole quotient.
    
    @staticmethod
    def percentage(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their percentage of a in b.
        Example: if we call Operations.percentage( 5.0, 20.0 ), it will return 25.0.
        """
        if b == 0: 
            return 0.0 # Return 0% if b is zero
        return ( a / b ) * 100 # This multiplies the two numbers and returns the result.
       
       
    @staticmethod
    def absolute_difference(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their absoulue difference.
        Just like the addition method, it expects two numbers and returns their result.
        Example: if we call Operations.absuloute_differnce(-4.0, 2.0), it will return 6.0.
        """
        return abs(a - b)  # This subtracts the second number (b) from the first number (a) and returns the absolute difference.
