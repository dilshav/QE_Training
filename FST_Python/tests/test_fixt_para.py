import pytest

#fixture from conftest
def test_functional(input_value):
    assert input_value<=40

#Paramaterized test: use the @pytest.mark.parameterize to provide multiple inputs to a single function
#@pytest.mark.parameterize(pattern, input_value)
@pytest.mark.parametrize("word", ["fetch","watch","fresh"])
def test_words(word):
    assert len(word)>=5

@pytest.mark.parametrize("num, expected_value", [(1,10),(2,20),(3,30)])
def test_num(num, expected_value):
    assert num*10 == expected_value