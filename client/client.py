#!/usr/bin/python

from sys import argv

from time import sleep
from requests import put
from psutil import cpu_percent


if __name__ == '__main__':
    sleep(0.5)  # Нужен что бы psutil успел получить правильный cpu_percent, а не 0

    server = None  # 127.0.0.1:8001

    try: server = argv[1]
    except IndexError: server = '127.0.0.1:5000'

    while True:
        cpu_load_percent = cpu_percent()

        try: put(f'http://{server}/api/handler', data={'cpu_load_percent': cpu_load_percent})
        except: pass

        sleep(10)
