#-*- coding: utf-8 -*-
from common.exceptions import CookingException
from common import sbanjum_constants as constants
from ingredients.jaeryo import Jaeryo

class Gogi(Jaeryo):
    cook_seconds:int = 0
    
    def __init__(self, amount):
        super().__init__("고기", amount)

    def pre_cook(self, cook_seconds):
        if cook_seconds <= 0:
            raise CookingException("0초 이상을 조리해 주세요.")
        self.cook_seconds = cook_seconds

    def cook(self, cook_seconds):
        self.cook_seconds = self.cook_seconds + cook_seconds
        if cook_seconds <= 0:
            raise CookingException("0초 이상을 조리해 주세요.")
        if cook_seconds >= 240 and cook_seconds < 320:  # 4~5분(240s~300s)
            self.taste = constants.TASTE_GOOD
        else: 
            self.taste = constants.TASTE_BAD
        self.status = constants.JAERYO_STATUS_FRIED
