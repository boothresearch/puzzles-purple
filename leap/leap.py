def leap_year(year):
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        print(True)
    else:
        print(False)

leap_year(1997) #False
leap_year(1996) #True
leap_year(1900) #False
leap_year(2000) #True


