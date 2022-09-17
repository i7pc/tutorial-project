# Створення функціїї та вивденення
"""def greeting():
    print("Hello world!")
greeting()
"""
# Виклик функції з передачею аргументу

"""
def invite_to_event(username):
    '''
    DOCSTRING: Information about this fuction
    INPUT: No Input
    OUTPUT: UserNave input
    '''
    return(f"Dear {username}, we have the honour to invite you to our event")


help(invite_to_event)
# Розрахунок тарифу для таксі
"""

""" Завдання підрахунку вартості таксі
base_rate = 40
price_per_km = 10
total_trip = 0


def trip_price(path):
    print("Hi, i'm work")
    global total_trip  # створення змінної для зміни в коді програми, по за межами ф-ції
    total_trip += 1  # лічильник виконання ф-ції

    return base_rate + price_per_km * path  # розрахунок
    # вивід інформації
    # return price_path
"""
"""v
# Завдання 3.4
def discount_price(price, discount):
    print("I'm work first")

    def apply_discount():
        print('I"m work second')
        nonlocal price
        return price * discount
    price = price - apply_discount()
    print(price)
    return price


discount_price(100, 0.1)

"""
"""
# Завдання 3.5 Повернення повного ім'я
def full_name(firs_name, last_name, midle_name = "") #полное имя

if midle_name:
    print(f"Your {first_name}")
else:
    print(f"You don't have name?")

# def get_fullname(first_name, last_name, midle_name = " "):
#    return
"""

"""v
def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        return (((length - len(string)) // 2) * " ") + string


format_string("abaa", 15)
^"""
"""v
def first(size, *args):
    return (size + len(args))


def second(size, **kwargs):
    return(size + len(kwargs))
^"""
# 8

"""v
def cost_delivery(quantity, *args, discount=0):
    result = (5+(quantity-1) * 2) * (1 - discount)
    return result

print(cost_delivery(2, 1, 2, discount=0.35))
^"""
# 10 Пошук кількості поєднаннь з n по k.
"""v
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# С = n! / ((n - k)! · k!) - формула


def numbers_of_groups(n, k):
    res = factorial(n)/(factorial(n - k) * factorial(k))
    return int(res)

print(numbers_of_groups(20, 3))
^"""
# 11 Пошук числа Фібоначі


"""v
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(7)
^"""
# 0, 1, 1, 2, 3, 5, 8, 13, 21
# Побудова ряду числа Фібоначі
"""v
f1 = f2 = 1
n = int(input("Enter number:"))
for i in range(2, n):
    f2 = f2+f1
    f1 = f2-f1
    print(f2, end=' ')  # end = " " допомогає записувати в рядок все що виводить
^"""

"""v
def fib(n):  # маємо передати значення n - як int(input("Enter number:"))
    if n == 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return fib(n-2)+fib(n-1)


print(fib(6))
^"""


def fib(n):  # маємо передати значення n - як int(input("Enter number:"))
    if n == 1 or n == 2:
        return 1
    # elif n == 2:
    #    return 1
    # else:
    return fib(n-2)+fib(n-1)


print(fib(6))


"""
#Знайти слово по тексту. Додаткове завдання
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
