import sys
sys.path.append("..")

from quizzes.module_1_quizzes import *
from quizzes.module_1_exercise_quizzes import *
import ipywidgets as widgets

import numpy as np
def square(x):
    return x**2

def add(x, y):
    return x + y

def print_name(first, last, middle=None):
    if middle is None:
        print(f"My name is {first.title()} {last.title()}")
    else:
        print(f"My name is {first.title()} {middle[0].title()}. {last.title()}")