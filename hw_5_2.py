import re
from typing import Callable

def generator_numbers(text: str):
    numbers = re.findall(r'\d+.\d',text)
    for number in numbers:
        yield number

def sum_profit(text: str, func: Callable):
        numbers = func(text)
        sum_num = 0
        for number in numbers:
            sum_num += float(number)
        return sum_num

