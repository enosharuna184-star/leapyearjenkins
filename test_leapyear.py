from leapYear import leapYear

def test_leapYear_pos():
    assert leapYear(2024) == True

def test_leapYear_zero():
    assert leapYear(2000) == True

def test_leapYear_neg():
    assert leapYear(2023) == False