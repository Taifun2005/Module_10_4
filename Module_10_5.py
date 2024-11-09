from multiprocessing import Pool
import time
import os

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

# spisok = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
    started_at = time.time()
    for filename in filenames:
        read_info(filename)

# thread1 = threading.Thread(target=read_info, args=(filenames, ))
# thread1.start()
    ended_at = time.time()
    elapsed = ended_at - started_at
    print(f'Функция работала {elapsed} ЛИНЕЙНЫЙ вызов')

# Многопроцессный
    started_at = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    # for
        # process1 = multiprocessing.Process(target=read_info, args=(spisok, ))
        # process1.start()
    ended_at = time.time()
    elapsed = ended_at - started_at
    print(f'Функция работала {elapsed} МНОГОПРОЦЕССОРНЫЙ вызов')


"""
from threading import  Thread, Event
import time

def first_worker():
    print("Первый рабочий приступил к своей задаче")
    event.wait()    #Ждет сигнал от события
    print("Первый рабочий продолжил выполнять задачу")
    time.sleep(5)
    print("Первый рабочий закончил выполнять задачу")

def second_worker():
    print("Второй рабочий приступил к своей задаче")
    time.sleep(10)
    print("Второй рабочий закончил выполнять задачу")
    event.set()     #Меняем значение флага event

event = Event()
thread1 = Thread(target=first_worker)
thread2 = Thread(target=second_worker)
thread1.start()
thread2.start()
# event.clear()     Сброс состояния флага

"""


"""
import multiprocessing
import time
import threading

counter = 0

def first_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(1)
        print("Первый рабочий запустил просес", counter)

    print('Первый рабочий изменил значение счетчика', counter)

def secong_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(1)
        print("Второй рабочий запустил просес", counter)
    print('Второй рабочий изменил значение счетчика', counter)


if __name__ == '__main__':
    process1 = multiprocessing.Process(target=first_worker, args=(10, ))
    process2 = multiprocessing.Process(target=secong_worker, args=(15, ))
    process1.start()
    process2.start()
"""

