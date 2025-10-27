# test_calculator.py
"""
This test module contains unit tests for the 'app/calculator.py' module.
Each test demonstrates good testing practices using the Arrange-Act-Assert (AAA) pattern.
AAA Pattern:
    - Arrange: No special setup required for this function.
    - Act: Call the display_help function.
    - Assert: Capture the output and verify it matches the expected help message.
"""

import pytest
from io import StringIO
from decimal import Decimal
import logging

import pytest
from unittest.mock import patch, Mock
from io import StringIO
from app.calculator import Calculator
from app.operations import OperationFactory
from app.calculator_repl import calculator_repl
from app.exception import OperationError, ValidationError



#test for calc operation
def test_calculator_repl():
    inputs = [
        "help", 
        "add", "9", "10",
        "exit"]

    #mock classes for operations
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output:

        #mock calculator return test sum
        m_calc = MockCalc.return_value
        m_calc.perform_operation.return_value = 19


        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for inputs
    assert "Calculator started" in output
    assert "Available commands:" in output
    assert "Enter numbers" in output
    assert "Result: 19" in output
    assert "Goodbye!" in output

#test for repl operation exception input
def test_validation_exception():

    inputs = [
        "add",
        "9",
        "b",
        "exit"]

    #mock classes for operations  
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output, \
         patch("app.calculator_repl.LoggingObserver"), \
         patch("app.calculator_repl.AutoSaveObserver"):
        
        m_calc = MockCalc.return_value
        #exception for for perform operation
        m_calc.perform_operation.side_effect = ValidationError("Error")

        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for inputs
    assert "Error:" in output
    assert "Goodbye!" in output

#test for repl operation exception input
def test_operation_exception():

    inputs = [
        "add",
        "9",
        "10",
        "exit"]

    #mock classes for operations  
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output, \
         patch("app.calculator_repl.LoggingObserver"), \
         patch("app.calculator_repl.AutoSaveObserver"):
        
        m_calc = MockCalc.return_value
        #exception for for perform operation
        m_calc.perform_operation.side_effect = Exception("Error")

        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for inputs
    assert "Unexpected error: Error" in output
    assert "Goodbye!" in output

#test for unknown command input
def test_unknown_command():
    inputs = [
        "test", 
        "exit"]

    #mock classes for operations
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output:


        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for inputs
    assert "Calculator started" in output
    assert "Unknown command" in output
    assert "Goodbye!" in output

#test for history operation
def test_history_repl():
    inputs = [
        "history", 
        "exit"]

    #mock classes for operations
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output:

        m_history = MockCalc.return_value
        m_history.show_history.return_value = ["9 + 10 = 19"]


        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for inputs
    assert "Calculator started" in output
    assert "Calculation History" in output
    assert "Goodbye!" in output


#test history commmand with no history
def test_no_history():

    inputs = [
        "history", 
        "exit"]

    #mock classes for operations
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output:

        m_history = MockCalc.return_value
        m_history.show_history.return_value = []


        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for inputs
    assert "Calculator started" in output
    assert "No calculations in history" in output
    assert "Goodbye!" in output


#test for repl clear operation
def test_clear_history():

    inputs = [
        "history",
        "clear",
        "exit"]

    #mock classes for operations
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output:

        m_history = MockCalc.return_value
        m_history.show_history.return_value = [" 9 + 10 = 19"]


        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for inputs
    assert "Calculator started" in output
    assert "Calculation History" in output
    assert "History cleared" in output
    assert "Goodbye!" in output


#test for undo and redo
def test_undo_redo_history():

    inputs = [
        "add", "9", "10",
        "undo",
        "redo",
        "exit"]

    #mock classes for operations
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output:

        #mock calculator that return sum of test inputs
        m_calc = MockCalc.return_value
        m_calc.perform_operation.return_value = 19

        #mock history undo redo
        m_history = MockCalc.return_value
        m_history.undo.return_value = True
        m_history.redo.return_value = True

        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for inputs
    assert "Calculator started" in output
    assert "Enter numbers" in output
    assert "Result: 19" in output
    assert "Operation undone" in output
    assert "Operation redone" in output
    assert "Goodbye!" in output


#test for undo and redo with no history
def test_undo_redo_no_history():

    inputs = [
        "redo",
        "undo",
        "exit"]


    #mock classes for operations
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output:


        m_do = MockCalc.return_value
        m_do.undo.return_value = False
        m_do.redo.return_value = False


        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for inputs
    assert "Calculator started" in output
    assert "Nothing to redo" in output
    assert "Nothing to undo" in output
    assert "Goodbye!" in output


#test for repl save input
def test_save():

    inputs = [
        "save",
        "exit"]

    #mock classes for operations  
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output, \
         patch("app.calculator_repl.LoggingObserver"), \
         patch("app.calculator_repl.AutoSaveObserver"):
        

        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for inputs
    assert "Calculator started" in output
    assert "History saved successfully" in output
    assert "Goodbye!" in output
    


#test for repl save input
def test_save_exception():

    inputs = [
        "save",
        "exit"]

    #mock classes for operations  
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output, \
         patch("app.calculator_repl.LoggingObserver"), \
         patch("app.calculator_repl.AutoSaveObserver"):
        
        m_calc = MockCalc.return_value
        #exception for save history
        m_calc.save_history.side_effect = Exception("Save Error")

        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for inputs
    assert "Calculator started" in output
    assert "Error saving history: Save Error" in output
    assert "Goodbye!" in output

#test for repl load input
def test_load():
    #test input
    inputs = [
        "load",
        "exit"]
    
    #mock classes for operations    
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output, \
         patch("app.calculator_repl.LoggingObserver"), \
         patch("app.calculator_repl.AutoSaveObserver"):
        
        m_calc = MockCalc.return_value
        #exception for save history
        m_calc.save_history.side_effect = Exception("Save Error")
        
        calculator_repl()
        output = fake_output.getvalue()

    assert "Calculator started" in output
    assert "History loaded successfully" in output
    assert "Goodbye!" in output


#test for repl load exception input
def test_load_exception():

    inputs = [
        "load",
        "exit"]

    #mock classes for operations  
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output, \
         patch("app.calculator_repl.LoggingObserver"), \
         patch("app.calculator_repl.AutoSaveObserver"):
        
        m_calc = MockCalc.return_value
        #exception for load history
        m_calc.load_history.side_effect = Exception("Load Error")

        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for inputs
    assert "Error loading history: Load Error" in output
    assert "Goodbye!" in output

#test for cancel operation
def test_cancel():
    #test inputs for cancel with 0 and 1 digit
    inputs = [
        "add",
        "cancel",
        "add", "9",
        "cancel",
        "exit"]

    #mock classes for operations    
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output, \
         patch("app.calculator_repl.LoggingObserver"), \
         patch("app.calculator_repl.AutoSaveObserver"):
        
    
        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for inputs
    assert "Calculator started" in output
    assert "Operation cancelled" in output
    assert "Enter numbers" in output
    assert "Operation cancelled" in output
    assert "Goodbye!" in output


#test for keyboard input exceptions
def test_kb_exception():
    #test inputs and exceptions
    inputs = [
        "help",
        KeyboardInterrupt,
        EOFError(),
        "exit"]

    #mock classes for operations   
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output, \
         patch("app.calculator_repl.LoggingObserver"), \
         patch("app.calculator_repl.AutoSaveObserver"):
        

        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for exceptions
    assert "Operation cancelled" in output
    assert "Input terminated. Exiting..." in output


def test_repl_exception():
    #test inputs and exceptions
    inputs = [
        Exception("Unexpected Error"),
        "exit"]

    #mock classes for operations   
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output, \
         patch("app.calculator_repl.LoggingObserver"), \
         patch("app.calculator_repl.AutoSaveObserver"):
        

        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for exceptions
    assert "Error: Unexpected Error" in output




    #test for exit input exception
def test_exit_kb_exception():
    #test inputs and exceptions
    inputs = [
        "exit"
        ]

    #mock classes for operations   
    with patch("app.calculator_repl.Calculator") as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output, \
         patch("app.calculator_repl.LoggingObserver"), \
         patch("app.calculator_repl.AutoSaveObserver"):
        
        m_calc = MockCalc.return_value
        #exception for save history
        m_calc.save_history.side_effect = Exception("Save Error")

        calculator_repl()
        output = fake_output.getvalue()

    #test assertions for exceptions
    assert "Goodbye!" in output
    assert "Warning: Could not save history: Save Error" in output

#test for exception interrupting calc repl
def test_calc_exception():
    exception= Exception("Error")
    inputs= []
    

    #mock classes for operations   
    with patch("app.calculator_repl.Calculator", side_effect= exception) as MockCalc, \
         patch("app.calculator_repl.OperationFactory") as MockFactory, \
         patch("builtins.input", side_effect= inputs), \
         patch("sys.stdout", new_callable=StringIO) as fake_output, \
         patch("app.calculator_repl.LoggingObserver"), \
         patch("app.calculator_repl.AutoSaveObserver"):
        

        with pytest.raises(Exception, match="Error"):
            calculator_repl()

        output = fake_output.getvalue()

    #test assertions for exceptions
    assert "Fatal error: Error" in output