# calculator_calculations.py

from abc import ABC, abstractmethod #abstract base class for specifying methods for subclasses
from app.operations import Operations #import operations classess from operations __init__

#Abstract Base Class: Calculation
class Calculation(ABC):
    """
    The Calculation abstract base class serves as a blueprint for the mathematical
    calculations in the calculator program. This class establishes a consistent 
    interface for all calculation types.   
    """

    #initialization for calculation instance with two operands a and b
    def __init__(self, a: float, b: float) -> None:

        #operands a and b stored as float
        self.a: float = a
        self.b: float = b

    @abstractmethod
    #abstract method used by subclasses to perform the calculations for requested operation.
    def execute(self) -> float: 
        pass # pragma: no cover


    #return string of calculation instance from input (operands, operation and result)
    def __str__(self) -> str:
        result = self.execute() #result of operation execute
        operation_name = self.__class__.__name__.replace('Calculation', '')  #operation name
        return f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}"


    #return technical representation of calculation instance for debugging (class name and operands)
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"


#-----------------------------------
#Factory Class: CalculationFactory
class CalculationFactory:
    """
    CalculationFactory is used to create instances of Calculation subclasses. 
    It allows for code orgaization and flexibility for adding new calculations.
    """

    # _calculations is a dictionary that holds a mapping of calculation types 
    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        """
        the register_caclculation decorator used to register a specific 
        Calculation subclass under a unique calculation type.
        """

        def decorator(subclass):
            #convert calculation type to lowercase
            calculation_type_lower = calculation_type.lower()

            #check if calculation type already exists, raise exception if true
            if calculation_type_lower in cls._calculations:
                raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
            
            #register new subclass in the _calculations dictionary
            cls._calculations[calculation_type_lower] = subclass

            return subclass  #return subclass for chaining or additional use
        return decorator  #returns decorator function.

    @classmethod
    def create_calculation(cls, calculation_type: str, a: float, b: float) -> Calculation:
        """
        the create_calculation class method creates instances of Calculation subclasses 
        using the calculation_type and float operands a and b
        """

        #convert calculation type to lowercase
        calculation_type_lower = calculation_type.lower()

        #get calculation from _calculations dictionary
        calculation_class = cls._calculations.get(calculation_type_lower)

        #raise exception if calculation type is not supported
        if not calculation_class:
            available_types = ', '.join(cls._calculations.keys())
            raise ValueError(f"Unsupported calculation type: '{calculation_type}'. Available types: {available_types}")
        
        #create and return instance of calculation with operands a and b
        return calculation_class(a, b)
#--------------------------------
# Concrete Calculation Classes
@CalculationFactory.register_calculation('add')
class AddCalculation(Calculation):
    """
    AddCalculation represents an addition operation between two numbers. 
    subclass uses execute method to perform addition from Operations module.
    """

    def execute(self) -> float:
        #calls addition method from Operations module to perform addition
        return Operations.addition(self.a, self.b)


@CalculationFactory.register_calculation('subtract')
class SubtractCalculation(Calculation):
    """
    SubtractCalculation represents a subtraction operation between two numbers.
    uses execute method to perform subtraction from Operations module.
    """

    def execute(self) -> float:
        #calls subtraction method from Operations module to perform subtraction
        return Operations.subtraction(self.a, self.b)


@CalculationFactory.register_calculation('multiply')
class MultiplyCalculation(Calculation):
    """
    MultiplyCalculation represents a multiplication operation.
    calls execute method to perform multiplication from Operations module.
    """

    def execute(self) -> float:
        #calls multiplication method from Operations module to perform the multiplication
        return Operations.multiplication(self.a, self.b)


@CalculationFactory.register_calculation('divide')
class DivideCalculation(Calculation):
    """
    DivideCalculation represents a division operation.
    
    **Special Case - Division by Zero**: Division requires extra error handling to 
    prevent dividing by zero, which would cause an error in the program. This class 
    checks if the second operand is zero before performing the operation.
    """

    def execute(self) -> float:
        #check if b operand is zero, raise exception if true
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        
        #calls division method from Operations module to perform division
        return Operations.division(self.a, self.b)
    

@CalculationFactory.register_calculation('power')
class PowerCalculation(Calculation):
    """
    PowerCalculation represents a power operation.
    calls execute method to perform power from Operations module.
    """

    def execute(self) -> float:
        #calls power method from Operations module to perform the power
        return Operations.power(self.a, self.b)