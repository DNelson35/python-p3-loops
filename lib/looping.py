#!/usr/bin/env python3
import time

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        time.sleep(1)
        counter -= 1
    print("Happy New Year!")

def square_integers(int_list):
    int_list = [int ** 2 for int in int_list]
    return int_list

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


happy_new_year()