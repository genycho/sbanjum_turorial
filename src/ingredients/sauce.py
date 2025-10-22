#-*- coding: utf-8 -*-
from common.exceptions import CookingException
from common import sbanjum_constants as constants
from ingredients.jaeryo import Jaeryo

class Chunjang(Jaeryo):
    def __init__(self, amount):
        super().__init__("춘장", amount)

    def cook(self, cook_seconds):
        if cook_seconds <= 0:
            raise CookingException("0초 이상을 조리해 주세요.")
        if cook_seconds >= 110 and cook_seconds < 140:  # 2분=120초 #FIXME    INJECTED 결함 
        # if cook_seconds <= 110 and cook_seconds > 140:  # 2분=120초 #FIXME    INJECTED 결함 
            self.taste = constants.TASTE_GOOD
        else: 
            self.taste = constants.TASTE_BAD
        self.status = constants.JAERYO_STATUS_BOILED

