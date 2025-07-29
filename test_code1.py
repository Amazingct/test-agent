import pytest
from code1 import add


class TestAdd:
    """Test cases for the add function in code1.py"""
    
    def test_integer_addition(self, capsys):
        """Test basic integer addition"""
        add(2, 3)
        captured = capsys.readouterr()
        assert captured.out.strip() == "5"
        
    def test_float_addition(self, capsys):
        """Test basic float addition"""
        add(2.5, 3.7)
        captured = capsys.readouterr()
        assert captured.out.strip() == "6.2"
        
    def test_mixed_number_addition(self, capsys):
        """Test integer and float addition"""
        add(2, 3.5)
        captured = capsys.readouterr()
        assert captured.out.strip() == "5.5"
        
    def test_string_to_int_conversion(self, capsys):
        """Test string that can be converted to integer"""
        add("2", "3")
        captured = capsys.readouterr()
        assert captured.out.strip() == "5"
        
    def test_string_to_float_conversion(self, capsys):
        """Test string that can be converted to float"""
        add("2.5", "3.7")
        captured = capsys.readouterr()
        assert captured.out.strip() == "6.2"
        
    def test_mixed_string_number_conversion(self, capsys):
        """Test mixing string numbers and actual numbers"""
        add("2", 3)
        captured = capsys.readouterr()
        assert captured.out.strip() == "5"
        
        add(2, "3")
        captured = capsys.readouterr()
        assert captured.out.strip() == "5"
        
    def test_string_concatenation_non_numeric(self, capsys):
        """Test string concatenation when strings can't be converted to numbers"""
        add("hello", "world")
        captured = capsys.readouterr()
        assert captured.out.strip() == "helloworld"
        
    def test_mixed_string_number_concatenation(self, capsys):
        """Test when one value is a non-numeric string and other is a number"""
        add("hello", 42)
        captured = capsys.readouterr()
        assert captured.out.strip() == "hello42"
        
        add(42, "world")
        captured = capsys.readouterr()
        assert captured.out.strip() == "42world"
        
    def test_scientific_notation(self, capsys):
        """Test scientific notation in strings"""
        add("1e3", "2e2")
        captured = capsys.readouterr()
        assert captured.out.strip() == "1200.0"
        
    def test_special_float_values(self, capsys):
        """Test special float values like inf and nan"""
        add("inf", "5")
        captured = capsys.readouterr()
        assert captured.out.strip() == "inf"
        
        add("nan", "5")
        captured = capsys.readouterr()
        assert captured.out.strip() == "nan"
        
    def test_negative_numbers(self, capsys):
        """Test negative number handling"""
        add("-5", "3")
        captured = capsys.readouterr()
        assert captured.out.strip() == "-2"
        
        add("-2.5", "-1.5")
        captured = capsys.readouterr()
        assert captured.out.strip() == "-4.0"
        
    def test_zero_handling(self, capsys):
        """Test zero handling"""
        add("0", "5")
        captured = capsys.readouterr()
        assert captured.out.strip() == "5"
        
        add(0, "0")
        captured = capsys.readouterr()
        assert captured.out.strip() == "0"
        
    def test_empty_string_handling(self, capsys):
        """Test empty string handling"""
        add("", "hello")
        captured = capsys.readouterr()
        assert captured.out.strip() == "hello"
        
        add("hello", "")
        captured = capsys.readouterr()
        assert captured.out.strip() == "hello"
        
    clear
        
    def test_boolean_inputs(self, capsys):
        """Test boolean inputs (which are subclass of int in Python)"""
        add(True, False)
        captured = capsys.readouterr()
        assert captured.out.strip() == "1"
        
        add(True, 5)
        captured = capsys.readouterr()
        assert captured.out.strip() == "6"
        
    def test_large_numbers(self, capsys):
        """Test very large numbers"""
        add("999999999999", "1")
        captured = capsys.readouterr()
        assert captured.out.strip() == "1000000000000"
        
    def test_decimal_precision(self, capsys):
        """Test decimal precision handling"""
        add("0.1", "0.2")
        captured = capsys.readouterr()
        # Note: This might have floating point precision issues
        result = float(captured.out.strip())
        assert abs(result - 0.3) < 1e-10
        
    def test_mixed_case_special_values(self, capsys):
        """Test case insensitive special values"""
        add("INF", "5")
        captured = capsys.readouterr()
        assert captured.out.strip() == "inf"
        
        add("NaN", "5")
        captured = capsys.readouterr()
        assert captured.out.strip() == "nan"


# Additional test functions for edge cases
def test_none_inputs():
    """Test that function handles None inputs gracefully"""
    with pytest.raises(AttributeError):
        # This should raise an error since None doesn't have isinstance behavior we expect
        add(None, 5)


def test_list_inputs():
    """Test non-standard input types"""
    with pytest.raises(TypeError):
        # This should raise an error since lists can't be added to numbers directly
        add([1, 2], 3)


if __name__ == "__main__":
    pytest.main([__file__]) 