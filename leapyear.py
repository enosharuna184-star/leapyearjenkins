import sys

def leapYear(year):
    if(year%4 == 0):
        return "Leap year"
    else:
        return "Not a Leap Year"
year = int(sys.argv[1])
leapYear(year)