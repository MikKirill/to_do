"""""""""
#   This is main class
Класс Task:
- Атрибуты:
  - id: int - идентификатор задачи
  - title: str - заголовок задачи
  - description: str - описание задачи
  - due_date: str - дата выполнения задачи

  - Методы:
    - create_task(): создание новой задачи
    - update_task(): обновление информации о задаче
    - delete_task(): удаление задачи
    - complete_task(): отметить задачу как выполненную
    - display_task(): отображение задачи
"""

'''
Класс Idea:
- Атрибуты:
  - id: int - идентификатор идеи
  - title: str - заголовок идеи
  - description: str - описание идеи

  - Методы:
    - create_idea(): создание новой идеи
    - update_idea(): обновление информации о идее
    - delete_idea(): удаление идеи
'''

'''
Класс Birthday:
- Атрибуты:
  - id: int - идентификатор дня рождения
  - name: str - имя человека, у которого день рождения
  - date: str - дата дня рождения

  - Методы:
    - create_birthday(): создание нового дня рождения
    - update_birthday(): обновление информации о дне рождения
    - delete_birthday(): удаление дня рождения
'''

'''
Класс TodoApp:
- Атрибуты:
  - tasks: list - список задач
  - ideas: list - список идей
  - birthdays: list - список дней рождения

  - Методы:
    - add_task(): добавление новой задачи в список
    - add_idea(): добавление новой идеи в список
    - add_birthday(): добавление нового дня рождения в список
    - get_all_tasks(): получение списка всех задач
    - get_all_ideas(): получение списка всех идей
    - get_all_birthdays(): получение списка всех дней рождения
'''