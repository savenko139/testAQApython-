"""

ДЗ 14. Расписание занятий

"""


import datetime

start_date = datetime.date(2022, 10, 17)
end_date = datetime.date(2023, 2, 3)
lectures_range = end_date - start_date
lectures_counter = 0

for i in range(lectures_range.days):
    dt = start_date + datetime.timedelta(i)
    if datetime.date.weekday(dt) == 0 or datetime.date.weekday(dt) == 3:
        lectures_counter += 1
        dt_str = datetime.datetime.strftime(dt, '%d %b %Y')
        print('Lecture {:>2}: {} 19:15'.format(lectures_counter, dt_str))
