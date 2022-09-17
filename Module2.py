"""
# Посчитать от одного до указанного числа
num = int(input("Enter the integer (0 to 100): "))
sum = 0

while num > 0:
    sum = num + sum
    num -= 1
    # print(sum)
print(sum)

# НОД найбільший дільник двох чисел #Завдання9
a = int(input("Enter the first integer: "))  # first
b = int(input("Enter the second integer: "))  # second
gcd = b if a > b else a

nod = 0

while True:
    if a % gcd == 0 and b % gcd == 0:
        nod = gcd
        print(nod)
        break
    else:
        gcd -= 1
        # print(gcd)
        continue

# Необходимо посчитать все числа от 1 до указанного числа и добавлять в сумму
# Нужно разобраться как строится задача, пояснить
num = int(input("Enter integer (0 for output): "))
sum = 0

while num != 0:
    for i in range(num+1):
        sum = i + sum
        i += 1
    print(sum)
    num = int(input("Enter integer (0 for output): "))

# num = int(input("Введите целое число (0 для выхода): "))

# 11 Теж саме тіки через переривання циклу break
sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    else:
        for i in range(num + 1):
            sum = sum + i
        print(sum)
# 12 Теж саме шо і №10 тіки беремо лише парні числа
sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    else:
        for i in range(num + 1):
            if i % 2 == 0:
                sum = sum + i
            else:
                continue
        print(sum)
"""
"""
# Код шифрования Цезаря
"""

"""
   message = input("Введите сообщение: ")  # Дане повідомлення, тип string
   # Зміщення для коду символа type integer
   offset = int(input("Введите сдвиг: "))
   encoded_message = ""
   # Для зсуву від а до z - № 97 - 122, A - 65, Z - 90 ! - 33
   # print(ord(message))
   for ch in message:
       pos_symb = ord(ch)
       # print(pos_symb)
       if 122 >= pos_symb >= 97:  # для роботи з нижнім регістром
           pos = ((pos_symb - ord('a')) + offset) % 26
           new_pos = pos + ord('a')
           encoded_message = encoded_message + chr(new_pos)
       elif 90 >= pos_symb >= 64:  # для роботи з верхнім регістром
           pos = ((pos_symb - ord('A')) + offset) % 26
           new_pos = pos + ord('A')
           encoded_message = encoded_message + chr(new_pos)
       else:  # для усіх інших випадків
           encoded_message = encoded_message + chr(pos_symb)

      # Зворотній код треба доробити
   # обратный код
   a = input("\n Wish you encode message? y/n")
   old_message = ""
   if a == "y":
   for ch in encoded_message:
       pos = ord(ch) - ord('a')
       old_pos = ((pos + ord('a')) - offset) % 26
       print(old_pos)
       # old_message = old_message + chr(old_pos)
   # print(old_message)
   else:
   print(f"Ok. You message is {encoded_message}")


   # pos = (pos + offset) % 26  # но позиція символу
   """
""" В чому сенс завдання?
pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
except ZeroDivisionError:
    print('Divide by zero completed!')
"""
# 15. Калькулятор специфічний
"""v

result = None
operand = None
operator = None
wait_for_number = True

while True:

    # перевірка на число
    x = input("Enter pls operand  ")
    try:
        operand = int(x)
    except ValueError:
        try:
            operand = float(x)
        except ValueError:
            print("Enter not number  ")
            continue
    print(result)
    # перевірка на введений символ після виконання введеня цифри
    symb = input("Enter pls operator  ")
    try:
"""


# Калькулятор з перевіркою відповідності введенням чисел і символів
result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number == True:  # Прапорец зміни введеня числових даних

        # №1 початок блоку перевірки введення числа
        x = input("Input operand - integer or float  ")
        try:
            operand = int(x)  # спроба перетворити значення в ціле
        except ValueError:
            try:
                operand = float(x)  # спроба перетворення в
            except ValueError:
                # не введено необхідний тип даних. Перетворення не можливе.
                print("Enter not number  ")
                continue  # Повернення на запит введеня необхідних даних
                # №1 кінець блоку перевірки введення числа

        # №2Блок логіки обробки даних.
        if result != None and operator != None:  # перевірка наявності даних в змінній та наявність оператора
            if y == "/":
                result = result / operand
            elif y == "*":
                result = result * operand
            elif y == "+":
                result = result + operand
            elif y == "-":
                result = result - operand
        else:  # при першому вводі є тільки одна цифра. Нема з чим обробляти
            result = operand
        # №2Блок логіки обробки даних.

        wait_for_number = False  # зміна прапорця. чекаємо на введеня символу

    elif wait_for_number == False:
        y = input("Input operator")  # логіка обробки введеноо символу
        # перевірка правильності введеного символу
        if y == ("/") or y == ("+") or y == ("-") or y == ("*") or y == ("="):

            if y == "=":  # запит отримання результату
                print(result)
                break
            else:  # якщо не було запиту результату
                operator = y
                wait_for_number = True
                continue
        else:  # якщо введений символ не відповідний, то необхідно повторити спробу
            print(f"{y} not '/' or '*' or '+' or '-'. Try again")
            continue
