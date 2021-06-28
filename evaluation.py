import random
from pprint import pprint
import math
from copy import deepcopy
import time
import traceback

import numpy as np

from simulated_annealing import *
from moves import *
import constraints 
from utils import *

def eval_solution(solution, input_data):
    score = 0
    c1, c2, c3, c4, c5 = (constraints.demand_constraint,                          
                        constraints.day_off_constraint,                          
                        constraints.length_work_blocks_constraint,                         
                        constraints.forbidden_constraint2,                          
                        constraints.forbidden_constraint3)
    
    if c1(solution, input_data): score += 20
    if c2(solution, input_data): score += 20
    if c3(solution, input_data): score += 20
    if c4(solution, input_data): score += 20
    if c5(solution, input_data): score += 20
    
    return score

def eval_solution_2(solution, input_data):
    score = 0
    c1, c2, c3, c4, c5 = (constraints.demand_constraint,                          
                        constraints.day_off_constraint,                          
                        constraints.length_work_blocks_constraint,                         
                        constraints.forbidden_constraint2,                          
                        constraints.forbidden_constraint3)
    if c1(solution, input_data): score += 50
    if c2(solution, input_data): score += 15
    if c3(solution, input_data): score += 15
    if c4(solution, input_data): score += 10
    if c5(solution, input_data): score += 10
    
    return score