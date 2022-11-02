from datetime import datetime, timedelta
from time import strftime

"""
1) Необхідно субботніх та недільних "Іменинників" привітати в наступний понеділок
"""
users = [
    {"name": "Monday_emp.", "birthday": datetime(year=1986, month=10, day=31)},
    {"name": "Thusday_emp.", "birthday": datetime(year=1986, month=11, day=1)},
    {"name": "Wednesday_emp.", "birthday": datetime(
        year=1986, month=11, day=2)},
    {"name": "Thersday_emp.", "birthday": datetime(
        year=1986, month=11, day=3)},
    {"name": "Friday_emp.", "birthday": datetime(year=1986, month=11, day=4)}
]


today_date = datetime(year=2022, month=11, day=1)

# отримуємо тиждень від введеної дати
for n in range(-2, 5):
    t_date = today_date + timedelta(days=n)  # перебираємо дні
    name_day = t_date.strftime("%A")
    birthday_name = []  # перелік іменинників
    b_name_str = ''  # строка виводу імен
    congratulation = ' '  # строка виводу привітання

    for employee in users:
        b_date = employee.get("birthday")
        if b_date.month == t_date.month and b_date.day == t_date.day:
            birthday_name.append(employee.get("name"))
            b_name_str = " ,".join(birthday_name)
    if t_date.weekday() == 5 or t_date.weekday() == 6:  # умова вихідних днів

    congratulation = (f'{name_day} : {b_name_str}')
    print(congratulation)


"""

# для "цього" тижня з урахуванням минулих вихідних
last_birthday = ""
for n in range(-2, 5):
    this_d = t_date + timedelta(days=n)
    name_day = this_d.strftime("%A")
    birthday_name = ""
    # перебираємо перелік аби дістати словники
    for employee in users:
        for b_name, b_date in employee.items():  # перебираємо значення
            b_month, b_day, b_year = b_date.split('-')
            norm_date = datetime(
                month=int(b_month),
                day=int(b_day),
                year=int(b_year)
            )

В понеділок - понеділок, субботу та неділю минулого тижня
"""

# if __name__ == "__main__":
#    get_birthdays_per_week(users)
