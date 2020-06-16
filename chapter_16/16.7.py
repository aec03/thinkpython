from datetime import date, datetime
import time

today = datetime.fromtimestamp(time.time())

def prompt_user():
    year = int(input('Birthday Year: '))
    month = int(input('Birthday Month: '))
    day = int(input('Birthday Day: '))

    return datetime(year, month, day)


def is_after(t1, today):
    if t1 < today:
        return True
    return False


def time_to_birthday(t1, today):
    t1 = t1.replace(year=today.year)
    if is_after(t1, today):
        t1 = t1.replace(year=today.year + 1)
    return abs(t1 - today)


def age(t1, today):
    if is_after(t1, today):
        return today.year - t1.year
    else:
        return today.year - t1.year + 1


my_birthday = prompt_user()
print(time_to_birthday(my_birthday, today))
print(age(my_birthday, today))