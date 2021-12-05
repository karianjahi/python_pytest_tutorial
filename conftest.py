"""
Creating a python module for test data and add a fixture decorator
"""
import pytest

text_file = "data/some_corpus.txt"

@pytest.fixture
def text_summary():
    with open(text_file, "r") as f:
        return f.read()

"""
- A class example
class MyFixture:
    def read_file(file):
        with open(file, "r") as f:
            return f.read()

@pytest.fixture
def text_summary():
    return MyFixture.read_file(text_file)
"""