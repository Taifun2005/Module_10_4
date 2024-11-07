"""
from queue import Queue
import time
import threading


def getter(queue):
    #while not queue.empty():
    while True:
        time.sleep(5)
        item = queue.get()  #.get() Достать из очередь
        print(threading.current_thread(), 'Взял элемент', item)


q = Queue(maxsize=10)
thread1 = threading.Thread(target=getter, args=(q,), daemon=True)
thread1.start()

for i in range(10):
    time.sleep(2)
    q.put(i)        #.put(i) Положить в очередь
    print(threading.current_thread(), 'Положил в очередь элемент', i)
"""



# q.put(5)
# print(q.get(timeout=3))
# print('Конец программы')
#
# mainTh = [537485]


from queue import Queue
import time
import threading
import random

class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest
class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = None
            for table in self.tables:
                if table.guest is None:
                    free_table = table
                    break

            if free_table is not None:
                free_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()