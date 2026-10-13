from leapyear import leapyear

def test_is():
    assert leapyear(2016) == True

def test_isnot():
    assert leapyear(2017) == False