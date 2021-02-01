import re
#DD/MM/YYYY format
date_regex = re.compile(r'''
(\d{2})\/             #day
(\d{2})\/             #month
(\d{4})               #year
''', re.VERBOSE)


while True:
    print('Input a day in DD/MM/YYYY format to check.')
    mo = date_regex.search(input())
    day = int(mo.group(1))
    month = int(mo.group(2))
    year = int(mo.group(3))
    leap_year = False
    valid_date = True

    #leap year check according to:
    #"divisible by 4, except divisible by 100 (unless also divisible by 400)"
    if year%4 == 0:
        leap_year = True
        if year%100 == 0:
            leap_year = False

    print('Day: ' + str(mo.group(1)))
    print('Month: ' + str(mo.group(2)))
    print('Year: ' + str(mo.group(3)))
    print('Leap Year: ' + str(leap_year))

    #year range check
    if year < 1000 or year > 2999:
        print('Invalid year.')
        valid_date = False

    #month range check
    if month < 1 or month > 12:
        print('Invalid month.')
        valid_date = False

    #day range check
    if day < 1 or day > 31:
        print('Invalid day.')
        valid_date = False

    #day specific checks
    if month in [4, 6, 9, 11]:
        if day > 30:
            print('Invalid day (30-day month).')
            valid_date = False
    elif month == 2:
        if leap_year == True and day > 29:
            print('Invalid day (leap year February).')
            valid_date = False
        elif day > 28:
            print('Invalid day (February).')
            valid_date = False

    #valid output
    if valid_date == True:
        print("This date is valid.")

    #TODO: add a 'what day of the week it was/will be' output alongside validity