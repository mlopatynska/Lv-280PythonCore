my_year = int(input("Please enter the year you want to check: "))
# we know that leap year is a year than can be divided on 4,
# except the age, that can not be divided on 400
# if year can not be divided on 4 means that this is a regular year
# if the year can be divided on 100 means that this is the century, so we have to check can it be divided on 400
# if this year can be divided on 400 means that it is leap year, if not - it is not leap year
# leap years examples:
# 1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836, 1840, 1844,
# 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896.
# 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956,
# 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996.
# 2000, 2004, 2008, 2012.
if (my_year % 4 == 0 and my_year % 100 != 0) or my_year % 400 == 0: # condition that means that the year is not regular
    print("it's a leap year")
else:
    print("this is not a leap year")

