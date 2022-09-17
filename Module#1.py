"""Пошук відстані між Києвом та Лондоном"""
"""import math

RADIUS_Earth = 6371.01

latitude_Kiev = 50.45
longtitude_Kiev = 30.523

latitude_London = 51.5072
longtitude_London = -0.1275

radian_latitude_Kiev = math.radians(latitude_Kiev)
radian_longtitude_Kiev = math.radians(longtitude_Kiev)
radian_latitude_London = math.radians(latitude_London)
radian_longtitude_London = math.radians(longtitude_London)

distance = RADIUS_Earth * math.acos(math.sin(radian_latitude_Kiev) * math.sin(radian_latitude_London) + math.cos(
    radian_latitude_Kiev) * math.cos(radian_latitude_London) * math.cos(radian_longtitude_Kiev - radian_longtitude_London))

print(distance)
"""

"""from unittest import result
is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
else:
    is_next = False
print(is_next) 
"""

"""
is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")
# is_admin = bool(is_admin)
# is_active = bool(is_active)
# is_permission = bool(is_permission)
access = True if is_admin or is_active and is_permission else False
можна ще одразу визначити бульовий тип значень для змінних
"""
"""
work_experience = int(input("Enter your full work experience in years: "))

if 1 < work_experience <= 5:
    developer_type = "Middle"
elif work_experience <= 1:
    developer_type = "Junior"
else:
    developer_type = "Senior"

print(developer_type)"""
"""
num = int(input("Enter a number: "))

if num > 0:
    if num % 2:
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"
print(result)
"""
"""
import math
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

D = b ** 2 - 4 * a * c
print(D)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(x1, x2)
elif D == 0:
    x1 = -(b/2*a)
    print(x1)
else:
    print("No answer's")
"""

"""
num = int(input("Enter an integer number: "))

is_even = False if num % 2 else True  # почему наоборот?!

print(is_even)
"""

"""
# Пошук к-сті символів у стрічці.
message = "NeveR aRgue with stupid people, they will dRag you down to theiR level and then beat you with expeRience."
search = "w"
result = 0
for i in message:
    if search == i:
        result += 1
print(result)
"""
