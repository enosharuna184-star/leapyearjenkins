import sys

def leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    year=int(sys.argv[1])
    print(f"{year} is {leapyear(year)}")
    print(sys.argv[0])