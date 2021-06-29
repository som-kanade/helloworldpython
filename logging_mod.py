#!/usr/bin/python 

import logging
import time
logger = logging.basicConfig(level=logging.DEBUG,format='%(name)s - %(asctime)s - %(levelname)s ; %(processName)s- %(message)s')

def add(x,y):
    return x+y 

def sub(x,y):
    return x-y 

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

added_result = add(5,4)
logging.warning("the sum is {}".format(added_result))
sub_result = sub(5,4)
logging.debug("the sub is {}".format(sub_result))
mul_result = sub(5,4)
logging.debug("the mul is {}".format(mul_result))
div_result = sub(5,4)
logging.error("the div is {}".format(div_result))