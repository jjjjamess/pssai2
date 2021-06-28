import random
from pprint import pprint
import math
from copy import deepcopy
import time
import traceback

import numpy as np

from simulated_annealing import *
from moves import *
from utils import *
from evaluation import *

def demand_constraint(result, input_data):
    for e in range(input_data['number_of_employees']):
        for d in range(input_data['length_of_schedule']):
            sum_day, sum_afternoon, sum_night = 0, 0, 0
            if result[e][d] == 'D': sum_day += 1
            elif result[e][d] == 'A': sum_afternoon += 1
            elif result[e][d] == 'N': sum_night += 1    
        
        if input_data['number_of_shifts'] > 2 :
            if  sum_day >= input_data['temporal_requirements_matrix'][0][d] and sum_afternoon >= input_data['temporal_requirements_matrix'][1][d] and sum_night >= input_data['temporal_requirements_matrix'][2][d]:
                pass
            else:
                return False
        else:
            if  sum_day >= input_data['temporal_requirements_matrix'][0][d] and sum_afternoon >= input_data['temporal_requirements_matrix'][1][d]:
                pass
            else:
                return False
    return True

def day_off_constraint(result, input_data):
    for e in range(input_data['number_of_employees']):
        count_dayoff = 0
        for d in range(input_data['length_of_schedule']):
            if result[e][d] == '-': count_dayoff += 1
        if input_data['min_days_off'] <= count_dayoff <= input_data['max_days_off']: pass
        else: return False
    return True

def length_work_blocks_constraint(result, input_data):
    for e in range(input_data['number_of_employees']):
        count_consecutive = 0
        min_flag, max_flag = False, False
        for d in range(input_data['length_of_schedule'] - 1):
            if result[e][d] != '-' and result[e][d+1] != '-': 
                count_consecutive += 1
                if count_consecutive >= input_data['min_length_work_blocks'] - 1:
                    min_flag = True
                    if count_consecutive <= input_data['max_length_work_blocks'] - 1:
                        max_flag = True
            else:  count_consecutive = 0
        if min_flag and max_flag: pass
        else: return False
    return True

def forbidden_constraint2(result, input_data):
    if input_data['not_allowed_shift_sequences_2'] == []: return True
    if input_data['not_allowed_shift_sequences_2'] != []:
        for e in range(input_data['number_of_employees']):
            for d in range(input_data['length_of_schedule'] - 1):
                for f in input_data['not_allowed_shift_sequences_2']:
                    if result[e][d] == f[0] and result[e][d+1] == f[1]: return False
        return True
    
def forbidden_constraint3(result, input_data):
    if input_data['not_allowed_shift_sequences_3'] == []: return True
    if input_data['not_allowed_shift_sequences_3'] != []:
        for e in range(input_data['number_of_employees']):
            for d in range(input_data['length_of_schedule'] - 2):
                for f in input_data['not_allowed_shift_sequences_3']:
                    if result[e][d] == f[0] and result[e][d+1] == f[1]                                             and result[e][d+2] == f[2]: return False
        return True
    