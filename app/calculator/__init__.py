import sys
from typing import List
from app.calculation import Calculation, CalculationFactory
import readline # Enables command history and editing in REPL

#REPL Calcualtor help message with program operations and input structure
def display_help() -> None:

    help_message = """
Calculator REPL Help
--------------------
Usage:
    <operation> <number1> <number2>
    - Perform a calculation with the specified operation and two numbers.
    - Supported operations:
        add       : Adds two numbers.
        subtract  : Subtracts the second number from the first.
        multiply  : Multiplies two numbers.
        divide    : Divides the first number by the second.
        power     : Raises the first number to the power of the second.
        root      : Calculates the nth root of a number.
        mod       : Returns the remainder of division of the first number by the second.
        intdivide : Performs integer division of the first number by the second.
        percent   : Calculates what percentage the first number is of the second.

Special Commands:
    help      : Display this help message.
    history   : Show calculation history.
    exit      : Exit the calculator.

Examples:
    add 10 5
    subtract 15.5 3.2
    multiply 7 8
    divide 20 4
    power 4 2
    root 4 2
    mod 10 3
    intdivide 10 3
    percent 5 20
    """
    print(help_message)

def display_history(history: List[Calculation]) -> None:
    """
    Displays the history of calculations performed during the session.
    """

    if not history:
        print("No calculations performed yet.")
    else:
        print("Calculation History:")
        for idx, calculation in enumerate(history, start=1):
            print(f"{idx}. {calculation}")

#REPL calculator that performs mathematical operations using calculation classes
def calculator() -> None:

    #repl calculator welcome message
    print("Welcome to the Professional Calculator REPL!")
    print("Type 'help' for instructions or 'exit' to quit.\n")

    #list to store calculation history
    history: List[Calculation] = []

    #calculator loop for input until manually exitted
    while True:
        try:
            # Prompt the user to enter an operation and two numbers
            user_input: str = input(">> ").strip()

            #if input empty restart loop
            if not user_input:
                continue # pragma: no cover

            #convert user input to lowercase 
            command= user_input.lower()

            #print help message if input is 'help'
            if command == 'help':
                display_help()
                continue  #restart loop

            if command == 'history':
                display_history(history)
                continue  #restart loop

            #exit program if input is 'exit'
            if command == 'exit':
                print("Exiting calculator. Goodbye!\n")
                sys.exit(0)  #break loop and exit program


            try:
                operation, num1_str, num2_str = user_input.split()

                #convert operand variable to float
                num1: float = float(num1_str)
                num2: float = float(num2_str)
            

            #exception handling for invalid input format
            except ValueError:
                print("Invalid input. Please follow the format: <operation> <num1> <num2>")
                print("Type 'help' for more information.\n")
                continue  #restart loop


           #create CalculationFactory instance for requested calcuation
            try:
                calculation = CalculationFactory.create_calculation(operation, num1, num2)


            #exception for unsupported operation
            except ValueError as ve:
                print(ve)
                print("Type 'help' to see the list of supported operations.\n")
                continue  # restart loop


            #excecute calculation
            try:
                result = calculation.execute()


            #exception for division by zero
            except ZeroDivisionError:
                print("Cannot divide by zero.")
                print("Please enter a non-zero divisor.\n")
                continue  # restart loop


            #exception for other unforeseen exceptions
            except Exception as e:
                print(f"An error occurred during calculation: {e}")
                print("Please try again.\n")
                continue  # restart loop

            # format result
            result_str: str = f"{calculation}"
            #print operation and result
            print(f"Result: {result_str}\n")

            #append calculation to history
            history.append(calculation)


            #restart loop


        #exception handling for keyboard interrupt
        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected. Exiting calculator. Goodbye!")
            sys.exit(0)

        #exception handling for EOF (Ctl+D)
        except EOFError:
            print("\nEOF detected. Exiting calculator. Goodbye!")
            sys.exit(0)


# If this script is run directly, start the calculator REPL
if __name__ == "__main__":
    calculator() # pragma: no cover