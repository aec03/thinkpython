from datetime import date
import time

def prompt_user():
    year = int(input('Birthday Year: '))
    month = int(input('Birthday Month: '))
    day = int(input('Birthday Day: '))
    print()

    return date(year, month, day)


def is_older(t1, t2):
    if t1 < t2:
        return (t1, t2)
    return (t2, t1)


def n_day(d1, d2, num=2):
    d1, d2 = is_older(d1, d2)
    day = abs(d2 - d1) / (num - 1) + d2
    return day


bday_1 = prompt_user()
bday_2 = prompt_user()
print(n_day(bday_1, bday_2, 4))