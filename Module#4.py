from random import randint
# 1 Створити список платежів. І їх порахувати сумму.
"""v
def amount_payment(payment):
    sum = 0
    for v in payment:
        if v < 0:
            continue
        else:
            sum += v
    return sum


# 2 Ф-ція яка видаляє max and min значення, сортує в порядку зростання і повертає змінений список

data = [21, 15, 27, 38, 64, 5, 2, 12]


def prepare_data(data):
    data.sort()  # сортування списку
    data.pop(0)  # видалення першого елементу
    data.pop(-1)  # видалення останнього елементу

    return data

print(prepare_data(data))
^"""
"""v
# Ф-ція як приймає список та видає строк з переліком #4.3
items = ["2 eggs", "1 liter sugar",  "1 tsp salt", "vinegar"]


def format_ingredients(items):
    # items = list(items) - якщо треба зробити нескінченну к-сть аргументів
    new_str = ""
    if len(items) > 1:
        l_e = items[-1]
        items.pop()
        items = items[::-1]

        while True:
            if len(items) > 1:
                new_str = new_str + items.pop() + ", "
            else:
                new_str = new_str + items.pop()
                break
        return new_str + " and " + l_e
    else:
        new_str = items.pop()
        return new_str

# Таж сама функція тільки менше строк
def format_ingredients(items):
    if len(items) > 1:
        l_e = items.pop(-1)
        new_str = ", ".join(items)
        return (new_str + " and " + l_e)
    else:
        new_str = "".join(items)
        return (new_str)


print(format_ingredients(items))
^"""

"""
# Знайти слово по тексту. Додаткове завдання
text = input("")
word = input("")


def search(text, word):
    # розділяємо в тексті кожне слово. Передаючи його в словник
    l_w_t = text.split(" ")
    w_f = None
    for i in l_w_t:
        if i == word:
            w_f = word
            break
        else:
            continue
    if w_f:
        return ("Word find")
    else:
        return ("Word not find")


print(search(text, word))
"""

"""v
# Визначення стипендії і запис в залікову книжку через словники
# key = F, FX, E, D, C, B, A. value1 = 1, 2, 3, 3, 4, 5, ,5. value2 =Unsatisfactorily, Enough, Satisfactorily, Good, Very good, Perfectly
grade = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
desription = {
    "F": "Unsatisfactorily",
    "FX": "Unsatisfactorily",
    "E": "Enough",
    "D": "Satisfactorily",
    "C": "Good",
    "B": "Very Good",
    "A": "Perfectly"}


def get_grade(key):
    if key in grade:
        x = grade[key]
        return x
    else:
        x = None
        return x


def get_description(key):
    if key in desription:
        x = desription[key]
        return x
    else:
        x = None
        return x
^"""

"""v
# Необхідно створити функцію яка перевіряє по значенням словника видає список ключів які відповідають цьому значенню.

data = {
    "Vadim": 1986,
    "Tanja": 1986,
    "Muza": 2017,
    "Vova": 2012,
    "Sofija": 2006,
    "Georgii": 2012
}

def lookup_key(data, value1):
    l = []
    for key, value in data.items():
        if value == value1:
            l.append(key)

        else:
            continue
    return l


print(lookup_key(data, 2002))
^"""

"""v
# 4.6 Перелік балів студентів. Знаходить середнє значення і ділить на 2 переліки - вище середнього і нище.
# grade = [112, 106, 192, 165, 173]
grade = []


def split_list(grade):
    sum = 0
    l_w = []  # list win
    l_s = []  # list looser
    # пошук межі розділення
    for v in grade:
        sum += v

    if len(grade) > 0:
        a_m = sum / len(grade)  # arithmetic mean

        for i in grade:
            if i > a_m:
                l_w.append(i)
            else:
                l_s.append(i)
    else:
        l_w = grade
        l_s = grade
    return l_w, l_s


^"""
"""v
# 4.7 пошук відстані по координатах
points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}
coordinates = [0, 1, 4, 2, 0]  # перевірочні координати


def calculate_distance(coordinates):
    distance = 0
 # блок коду для створення переліку по якому буде перевірка дистанції
    n = 0
    i = 1
    while i < len(coordinates):
        s_c = coordinates[n:n+2]  # slice list
        n += 1
        i += 1
        # б.к. аби перше значення завжди було менше другого
        if s_c[0] < s_c[1]:
            s_c = s_c

        else:
            s_c = s_c[::-1]
        s_c = tuple(s_c)
        # б.к. для порівняня ключа і створеної дистанції, координат.
        for key in points.keys():
            if s_c == key:
                v = points.get(key)
                distance += v
            else:
                continue
    return round(distance, 1)

print(calculate_distance(coordinates))
^"""

"""v
# 4.8 Змійка?

terra = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
power = 1

def game(terra, power):
    for l in terra:
        for n in l:
            if n <= power:
                power = power + n
            else:
                break
    return power


^"""
# 4.9 Перевірка пінкоду

"""v
def is_valid_pin_codes(pin_codes):
    ans = None
    if len(pin_codes) > 0:
        for p in p_c:
            x = p_c.count(p)
            if x == 1 and type(p) == str and len(p) == 4:
                for i in p:
                    if 48 <= ord(i) <= 57:
                        continue
                    else:
                        ans = False  # return for function
                        break
                continue
            else:
                ans = False  # return for function
                break  # return for function
    else:
        ans = False

    if ans == None:
        return True
    else:
        return False

^"""

"""v
# 4.10 Згенерувати випадковий пароль довжиною 8м символів
def get_random_password():
    m_s = ""  # my string
    while len(m_s) < 8:
        r_s = chr(randint(40, 126))  # random numbder in ASCII
        m_s += r_s
    return m_s
^"""

"""v
# 4.11 Надійність пароля
# Довжина рядка пароля вісім символів.
# Містить хоча б одну літеру у верхньому регістрі.
# Містить хоча б одну літеру у нижньому регістрі.
# Містить хоча б одну цифру.

def is_valid_password(password):
    U_x = None
    l_x = None
    n_x = None
    if not len(password) >= 8:
        return print(False)
    for i in password:
        x = ord(i)
        if 90 >= x >= 65:
            U_x = x  # Upper
        if 122 >= x >= 97:
            l_x = x  # lower
        if 57 >= x >= 48:
            n_x = x  # number
    if (U_x == None) or (l_x == None) or (n_x == None):
        return print(False)
    return print(True)
^"""

# 4.12 Генерує код, поки не згенерує пормальний. З урахування ф-цій з попередніх завдань 4.10 та 4.11

"""v
def get_password():

    try_n = 0
    result = False
    while not result or try_n < 100:
        password = get_random_password()
        # print(password)
        result = is_valid_password(password)
        # print(result)
        try_n += 1
        if result != True and try_n <= 10:
            continue
        elif result == True:
            return print(password)
        elif try_n > 100:
            return False

^"""
# 4.13 - знайти шлях до файлу і вивести їх назву та назву тек.
