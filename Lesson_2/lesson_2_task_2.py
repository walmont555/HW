def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


print("год 2020:", is_year_leap(2020))
print("год 2021:", is_year_leap(2021))