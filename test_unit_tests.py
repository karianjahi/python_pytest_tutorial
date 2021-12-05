# Unit tests
from itertools import count
import pytest
from word_counter import count_words

class TestWordCounter:
    def test_count_words(self):
        """
        We need to test the function count_words
        """
        text = "Today is Monday"
        assert count_words(text) == 3
        

    def test_single_word(self):
        """
        Single word test
        """
        text = "head"
        assert count_words(text) == 1
    
    def test_two_words(self):
        text = "He jumps"
        assert count_words(text) == 2
        
    def test_linebreaks(self):
        text = "He\nis\nnot\nfeeling\nwell"
        assert count_words(text) == 5
    
    def test_accents(self):
        text = "Mein Hände"
        assert count_words(text) == 2
        
    def test_html(self):
        text = '<h1>This is a heading</h1>'
        assert count_words(text) == 4
    
    def test_html_with_attributes(self):
        text = '<h1 class="foo">this is a heading</h1>'
        assert count_words(text) == 5
    
    def test_dashes(self):
        text = "Joseph-Njeri"
        assert count_words(text) == 2
        
        
class TestWordCounterExceptions:
        def test_raise_type_error(self):
            """
            When text is not of type string
            """
            text = {"Ketan": "studies data science at spiced"}
            with pytest.raises(TypeError) as te:
                assert count_words(text) == 5
            assert "word counter accepts only strings" in str(te.value)


# Parametrized tests: Run many tests in one
class TestWordCounterParametrization:
    """
    In this case we want to test many tests in one function
    """
    
    Tests = [
        ("Today is Monday", 3),
        ("head", 1),
        ("He jumps", 2),
        ("He\nis\nnot\nfeeling\nwell", 5),
        ("Mein Hände", 2),
        ('<h1>This is a heading</h1>', 4),
        ('<h1 class="foo">this is a heading</h1>', 5),
        ("Joseph-Njeri", 2)
        ]
    
    @pytest.mark.parametrize('input, output', Tests)
    def test_all_in_one(self, input, output):
        """
        Testing all in one
        """
        assert count_words(input) == output









    