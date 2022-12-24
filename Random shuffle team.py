import random  # модуль випадковості вибору

team = []
while True:
    # запускаємо нескінченний цикл введення членів команди
    member = input("Enter Name of the member or enter end for finisch: ")
    if member == 'end':
        break
    team.append(member)
iterable_operation = len(team)

while 0 < iterable_operation:
    # цикл витягує ім"я
    random.shuffle(team)  # перемішує перелік
    member_of_team = team.pop()  # витягає ім"я
    # виводить номер, через крапку ім"я
    print(iterable_operation, '.', member_of_team)
    iterable_operation -= 1
