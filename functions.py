import texts
from random import randint

def parse_digits_from_text(text):
    digit = ""
    for i in text:
        if i.isdigit():
            digit += i
    return int(digit)

def send_task_for_lab(number):
    if (0 < number < 8):
        return texts.labs_and_links[number]
    else:
        return "Лабораторну роботу не знайдено ☹️"

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)