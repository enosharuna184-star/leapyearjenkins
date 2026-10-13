import sys

def leapYear(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

if __name__ == "__main__":
    year = int(sys.argv[1])
    print("Leap year:", leapYear(year))