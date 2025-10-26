########################
# Calculator REPL       #
########################

from decimal import Decimal
import logging

from app.calculator import Calculator
from app.exception import OperationError, ValidationError
from app.history import AutoSaveObserver, LoggingObserver
from app.operations import OperationFactory

from colorama import Fore, Back, Style


def calculator_repl():
    """
    Command-line interface for the calculator.

    Implements a Read-Eval-Print Loop (REPL) that continuously prompts the user
    for commands, processes arithmetic operations, and manages calculation history.
    """
    try:
        # Initialize the Calculator instance
        calc = Calculator()

        # Register observers for logging and auto-saving history
        calc.add_observer(LoggingObserver())
        calc.add_observer(AutoSaveObserver(calc))

        print("Calculator started. Type 'help' for commands.")

        while True:
            try:
                print(Style.RESET_ALL)
                # Prompt the user for a command
                command = input("\nEnter command: ").lower().strip()
                print(Style.RESET_ALL)

                if command == 'help':
                    # Display available commands
                    print(Style.BRIGHT + Fore.YELLOW + "\nAvailable commands:")
                    print(Style.BRIGHT + Fore.YELLOW +"  add, subtract, multiply, divide, power, root, mod, int_divide, percent, abs_diff - Perform calculations")
                    print(Style.BRIGHT + Fore.YELLOW +"  history - Show calculation history")
                    print(Style.BRIGHT + Fore.YELLOW +"  clear - Clear calculation history")
                    print(Style.BRIGHT + Fore.YELLOW +"  undo - Undo the last calculation")
                    print(Style.BRIGHT + Fore.YELLOW +"  redo - Redo the last undone calculation")
                    print(Style.BRIGHT + Fore.YELLOW +"  save - Save calculation history to file")
                    print(Style.BRIGHT + Fore.YELLOW +"  load - Load calculation history from file")
                    print(Style.BRIGHT + Fore.YELLOW +"  exit - Exit the calculator")
                    print(Style.RESET_ALL)
                    continue

                if command == 'exit':
                    # Attempt to save history before exiting
                    try:
                        calc.save_history()
                        print(Style.BRIGHT+ Fore.CYAN +"History saved successfully.")
                    except Exception as e:
                        print(Style.BRIGHT+ Fore.RED +f"Warning: Could not save history: {e}")
                    print(Style.RESET_ALL)    
                    print("Goodbye!")
                    break

                if command == 'history':
                    # Display calculation history
                    history = calc.show_history()
                    if not history:
                        print(Style.DIM+ Fore.RED +"No calculations in history")
                    else:
                        print(Style.BRIGHT+ Fore.BLUE +"\nCalculation History:")
                        for i, entry in enumerate(history, 1):
                            print(Style.BRIGHT+ Fore.BLUE +f"{i}. {entry}")
                    continue

                if command == 'clear':
                    # Clear calculation history
                    calc.clear_history()
                    print(Style.BRIGHT+ Fore.BLUE +"History cleared")
                    continue

                if command == 'undo':
                    # Undo the last calculation
                    if calc.undo():
                        print(Style.BRIGHT+ Fore.CYAN +"Operation undone")
                    else:
                        print(Style.DIM + Fore.CYAN +"Nothing to undo")
                    continue

                if command == 'redo':
                    # Redo the last undone calculation
                    if calc.redo():
                        print(Style.BRIGHT+ Fore.CYAN +"Operation redone")
                    else:
                        print(Style.BRIGHT+ Fore.CYAN +"Nothing to redo")
                    continue

                if command == 'save':
                    # Save calculation history to file
                    try:
                        calc.save_history()
                        print("History saved successfully")
                    except Exception as e:
                        print(Style.BRIGHT+ Fore.RED +f"Error saving history: {e}")
                    continue

                if command == 'load':
                    # Load calculation history from file
                    try:
                        calc.load_history()
                        print("History loaded successfully")
                    except Exception as e:
                        print(Style.BRIGHT+ Fore.RED +f"Error loading history: {e}")
                    continue

                if command in ['add', 'subtract', 'multiply', 'divide', 'power', 'root', 'mod', 'int_divide', 'percent', 'abs_diff']:
                    # Perform the specified arithmetic operation
                    try:
                        print("\nEnter numbers (or 'cancel' to abort):")
                        a = input("First number: ")
                        if a.lower() == 'cancel':
                            print(Style.BRIGHT+ Fore.RED+ "Operation cancelled")
                            continue
                        b = input("Second number: ")
                        if b.lower() == 'cancel':
                            print(Style.BRIGHT+ Fore.RED+ "Operation cancelled")
                            continue

                        # Create the appropriate operation instance using the Factory pattern
                        operation = OperationFactory.create_operation(command)
                        calc.set_operation(operation)

                        # Perform the calculation
                        result = calc.perform_operation(a, b)

                        # Normalize the result if it's a Decimal
                        if isinstance(result, Decimal):
                            result = result.normalize()

                        print(Style.BRIGHT + Back.GREEN + f"\nResult: {result}")
                    except (ValidationError, OperationError) as e:
                        # Handle known exceptions related to validation or operation errors
                        print(Style.BRIGHT+ Fore.RED + f"Error: {e}")

                    except Exception as e:
                        # Handle any unexpected exceptions
                        print(Style.BRIGHT+ Fore.RED + f"Unexpected error: {e}")
                    continue

                # Handle unknown commands
                print(Style.DIM + Fore.RED + f"Unknown command: '{command}'. Type 'help' for available commands.")

            except KeyboardInterrupt:
                # Handle Ctrl+C interruption gracefully
                print(Style.BRIGHT+ Fore.RED +"\nOperation cancelled")
                continue
            except EOFError:
                # Handle end-of-file (e.g., Ctrl+D) gracefully
                print(Style.BRIGHT+ Fore.RED +"\nInput terminated. Exiting...")
                break
            except Exception as e:
                # Handle any other unexpected exceptions
                print(Style.BRIGHT+ Fore.RED +f"Error: {e}")
                continue

    except Exception as e:
        # Handle fatal errors during initialization
        print(Style.BRIGHT+ Back.RED +f"Fatal error: {e}")
        logging.error(Style.BRIGHT+ Back.RED +f"Fatal error in calculator REPL: {e}")
        raise
