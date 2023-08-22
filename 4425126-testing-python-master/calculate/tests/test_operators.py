from calculate.operators import Operators

def test_should_make_multiple_addition():
    sut = Operators()
    operation = "5.5 + 10 + 30 + 13.7"
    expected_value = 59.2
    assert sut.addition(operation) == expected_value

def test_should_make_multiple_substraction():
    sut = Operators()
    operation = "10-1-2-7"
    expected_value = 0
    assert sut.substraction(operation) == expected_value

def test_should_make_multiple_multiplication():
    sut = Operators()
    operation = "1*2*3*4"
    expected_value = 24
    assert sut.multiplication(operation) == expected_value

def test_should_make_multiple_division():
    sut = Operators()
    operation = "1/2/2"
    expected_value = 0.25
    assert sut.division(operation) == expected_value

def test_is_operation_valid():
    sut = Operators()



# def test_is_symbol_valid(symbol, signe):
#     sut = Operators()
#     symbols = [symbol for symbol in self.operation if not symbol.isdigit()]
#     operation = symbol != signe and symbol != "." and symbol != " "
#     expected_value = False
#     assert sut._is_symbol_valid() == expected_value