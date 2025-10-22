#-*- coding: utf-8 -*-
from common.exceptions import CookingException
from common import sbanjum_constants as constants
from ingredients.jaeryo import Jaeryo

class Myun(Jaeryo):
    def __init__(self, amount):
        super().__init__("면", amount)

    def cook(self, cook_seconds):
        if cook_seconds <= 0:
            raise CookingException("0초 이상을 조리해 주세요.")

        if cook_seconds >= 290 and cook_seconds < 310:  # 5분=300초 
            self.taste = constants.TASTE_GOOD
        else: 
            self.taste = constants.TASTE_BAD
        self.status = constants.JAERYO_STATUS_BOILED
