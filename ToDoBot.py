HELP = """
***

help - вывести справку по использованию
add - добавить новую задачу
show - вывести все добавленные задачи на конкретную дату
dates - вывести даты, на которые есть задачи
tasks - вывести все задачи
task - добавить быструю задачу

***"""

tasks = {

}

def add_task(date, task):
    if date in tasks:  #  Если дата есть в словаре, то добавляем задачу по ключу даты
        tasks[date].append(task)
    else:  # Если даты нет в словаре, то создаем дату и добавляем задачу по ключу даты
        tasks[date] = []
        tasks[date].append(task)
    print(f'Задача "{task}" добавлена на дату: {date}')

run = True

while run:
    print(HELP)
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("Задач на эту дату нет.")
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        add_task(date, task)
    elif command == "dates":
        if len(tasks) > 0:
            for date in tasks.keys(): 
                print(date)
        else:
            print("Нет запланированных задач.")
    elif command == "tasks":
        if len(tasks) > 0:
            for key, value in tasks.items():
                print(f'{key}: {value}')
        else:
            print("Нет запланированных задач.")
    elif command == "exit":
        print("Программа остановлена.")
        run = False
    else: 
        print("Неизвестная команда! Введите доступную команду!")

