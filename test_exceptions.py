import pytest
from word_counter import count_words
class TestWordCounterExceptions:
    """
    Testing exceptions
    """
    def test_raise_type_error(self):
        """
        When text is not of type string
        """
        text = {"Ketan": "studies data science at spiced"}
        with pytest.raises(TypeError) as type_error:
            assert count_words(text) == 5
        assert "word counter accepts only strings" in str(type_error.value)