import sys
import pandas
sys.path.append("..")

from quizzes.module_4_quizzes import *
# from quizzes.module_4_exercise_quizzes import *

import ipywidgets as widgets

import numpy as np

import pymysql
import getpass

def connect_to_mimic(user="uu-phs"):
    return pymysql.connect(host="35.233.174.193",port=3306,
                       user=user,passwd=getpass.getpass("Enter password for MIMIC2 database"),
                       db='mimic2')
