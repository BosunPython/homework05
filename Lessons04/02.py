from datetime import datetime
from time import sleep

def clock(b):
    list1 = []
    for i in range(b):
        dt_now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S,')
        sleep(sec)
        i = dt_now
        list1.append(i)
    return list1
n = int(input("Введите значение переменной: "))
sec = int(input("Введите кол-во секунд: "))
print(clock(n))
