#-*- coding: utf-8 -*-
from common.exceptions import CookingException
from common import sbanjum_constants as constants
from ingredients.jaeryo import Chaeso

class Yangpa(Chaeso):
    def __init__(self, amount):
        super().__init__("양파", amount)

    def cook(self, cook_seconds):
        if cook_seconds <= 0:
            raise CookingException("0초 이상을 조리해 주세요.")
        # self.status = constants.JAERYO_STATUS_FRIED   #INJECTED. 실제 코드 결함 사례
        if self.status == constants.JAERYO_STATUS_SLICED and self.sliced_size == constants.SIZE_MEDIUM and cook_seconds >= 110 and cook_seconds < 130:  # 2분=120초 
            self.taste = constants.TASTE_GOOD
        else: 
            self.taste = constants.TASTE_BAD
        self.status = constants.JAERYO_STATUS_FRIED

class Gamja(Chaeso):
    def __init__(self, amount):
        super().__init__("감자", amount)
		
    def cook(self, cook_seconds):
        if cook_seconds <= 0:
            raise CookingException("0초 이상을 조리해 주세요. ")
        if self.status == constants.JAERYO_STATUS_SLICED and self.sliced_size == constants.SIZE_MEDIUM and cook_seconds >= 110 and cook_seconds < 130:  # 2분=120초 
            self.taste = constants.TASTE_GOOD
        else: 
            self.taste = constants.TASTE_BAD
        self.status = constants.JAERYO_STATUS_FRIED
		
class Hobak(Chaeso):
    def __init__(self, amount):
        super().__init__("호박", amount)

    def cook(self, cook_seconds):
        if cook_seconds <= 0:
            raise CookingException("0초 이상을 조리해 주세요. ")
        # if self.status == constants.JAERYO_STATUS_SLICED and self.sliced_size == constants.SIZE_MEDIUM and cook_seconds >= 80 and cook_seconds < 100:  # FIXME 요건 변경. 1분30초=90초 
        if self.status == constants.JAERYO_STATUS_SLICED and self.sliced_size == constants.SIZE_MEDIUM and cook_seconds >= 110 and cook_seconds < 130:
            self.taste = constants.TASTE_GOOD
        else: 
            self.taste = constants.TASTE_BAD
        self.status = constants.JAERYO_STATUS_FRIED