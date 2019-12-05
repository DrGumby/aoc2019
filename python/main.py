#!/usr/bin/env python3

from tasks import *

def run_task(cls):
    cls.run()

if __name__ == "__main__":
    tasks = [day5.Ex9()]
    for task in tasks:
        print("Name: {0}\nValue: {1}\n".format(task.name, task.run()))
