print('=======DNI DO KONCA ROKU ======')
#ile dni do konca roku

def DaysToYearEnd():
    import datetime
    date_today = datetime.date.today()
    print('dzisiaj mamy ',date_today)
    current_year = date_today.year
    print('obecny rok to : ',current_year)
    date_end_year = datetime.date(current_year,12,31)
    print(date_end_year)
    delta = date_end_year-date_today
    print('Do konca roku zostało dni : ',delta.days)

DaysToYearEnd()

print('=======DNI DO KONCA ROKU v2======')
#ile dni do konca roku

def DaysToEndOfYear(year, month, day):
    from datetime import date

    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)


DaysToEndOfYear(2020, 12, 20)
DaysToEndOfYear(2021, 12, 21)
DaysToEndOfYear(year=2022, month=12, day=22)
DaysToEndOfYear(day=23, month=12, year=2023)

print('=======DNI DO KONCA ROKU v3======')

from datetime import date


def DaysToEndOfYear(year=date.today().year,
                    month=date.today().month,
                    day=date.today().day):
    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print('Counting from ', date_today, 'days remaining', delta.days)


DaysToEndOfYear(2020, 12, 20)
DaysToEndOfYear(day=23, month=12, year=2023)
DaysToEndOfYear()
DaysToEndOfYear(year=2020)
DaysToEndOfYear(year=2020, month=10)
DaysToEndOfYear(day=1)

print('=======DNI DO KONCA ROKU v4======')

from datetime import date


def DaysToEndOfYear(year=date.today().year,
                    month=date.today().month,
                    day=date.today().day):
    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    return delta.days


print('Date: 2020-12-20 days to end of year: %d' % (DaysToEndOfYear(2020, 12, 20)))

print('Date: 2020-12-21 days to end of year: %d' % (DaysToEndOfYear(2020, 12, 21)))

print('Date: TODAY days to end of year: %d' % (DaysToEndOfYear()))

from datetime import date

print('=======DNI DO KONCA ROKU v5======')

def DaysToEndOfYear(*dates):
    for date_today in dates:
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print('Date', date_today, 'days to end of year', delta.days)


DaysToEndOfYear(date(1999, 1, 15))
print('----------------')
DaysToEndOfYear(date(1999, 1, 15), date(2009, 1, 15))
print('----------------')
DaysToEndOfYear(date(1999, 1, 15), date(2009, 1, 15), date(2019, 1, 15))
print('----------------')
DaysToEndOfYear(date(1999, 1, 15), date(2009, 1, 15), date(2019, 1, 15), date.today())