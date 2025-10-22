#-*- coding: utf-8 -*-
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common_logger import logger

class SBanjumException(Exception):
    """ a custom exception for error handling """
    def __init__(self, message):
        self.value = message

    def __str__(self):
        logger.warning(f"SbanjumException - {self.value}")
        return self.value
    
class CookingException(Exception):
    """ a custom exception for error handling """
    def __init__(self, message):
        self.value = message

    def __str__(self):
        logger.warning(f"CookingException - {self.value}")
        return self.value
