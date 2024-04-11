import unittest
from typing import NoReturn

from src.calculator import Calculator
from src.custom_ex import IncorrectInputError


class CalculatorAddTestCase(unittest.TestCase):  # Test Case
    
    def test_add_3_corrrect_input(self) -> None | NoReturn:  # Unit
        # Arrange
        calculator = Calculator()
        x = 4
        y = 3
        z = 1
        expected_result = 8

        # Act
        result = calculator.add(x, y, z)

        # Assert
        self.assertEqual(result, expected_result)



    def test_add_with_incorrect_input(self) -> NoReturn:
        # Arrange
        calculator = Calculator()
        x = "6"
        y = [4, 5]

        # Act/Assert
        with self.assertRaises(TypeError):
            calculator.add(x, y)

    def test_add_with_no_args(self) -> None | NoReturn:
        # Arrange
        calculator = Calculator()
        expected_result = 0

        # Act
        result = calculator.add()

        # Assert
        self.assertEqual(result, expected_result)



class CalculatorMultTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_mult_with_correct_input(self):
        # Arrange
        x = 1
        y = 2
        z = 3
        expected_result = 6

        # Act
        result = self.calculator.multiply(x, y, z)

        # Assert
        self.assertEqual(result, expected_result)

    def test_mult_with_incorrect_input(self):
        # Arrange
        x = []
        y = (1, 2)
        z = "4"

        # Act/Assert
        with self.assertRaises(IncorrectInputError):
            self.calculator.multiply(x, y, z)

    # def test_mult_with_no_input(self): 
    #      # Arrange
    #     expected_result = None

    #     # Act
    #     result = self.calculator.multiply()

    #     # Assert
    #     self.assertEqual(result, expected_result)    
           

    def tearDown(self):
        pass


class CalculatorDivTestCase(unittest.TestCase): 
    def setUp(self):
        self.calculator = Calculator()

    def test_div_with_correct_input(self):
        #Arrange
        x=20
        y=4
        expected_result=5

        result=self.calculator.division(x,y)

        self.assertEqual(result,expected_result)
    

    def test_div_with_incorrect_input(self):
        #Arrange
        x="3"
        y="a"
        
        #Act Assert
        with self.assertRaises(TypeError):
            self.calculator.division(x,y)

    # def test_div_with_no_input(self):

    #     #Arrange
    #     result=self.calculator.division()
    #     expected_result=0
    #     self.assertEqual(result,expected_result)  

    
    def tearDown(self):
        pass
    

        

            