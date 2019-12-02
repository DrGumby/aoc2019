#!/usr/bin/env python3

from tasks import *

def run_task(cls):
    cls.run()

if __name__ == "__main__":
    tasks = [day1.Ex1(), day1.Ex2(), day2.Ex3(), day2.Ex4()]
    for task in tasks:
        print("Name: {0}\nValue: {1}\n".format(task.name, task.run()))