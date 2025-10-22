#-*- coding: utf-8 -*-
from common.exceptions import CookingException
from common.exceptions import SBanjumException
from common import sbanjum_constants as constants
from common import recipe
from ingredients.vegetables import Yangpa
from ingredients.vegetables import Gamja
from ingredients.vegetables import Hobak
from ingredients.noodles import Myun
from ingredients.sauce import Chunjang
from ingredients.pork_meat import Gogi
# from pydantic import BaseModel

class FoodItems():
    yangpa:Yangpa=None
    gamja:Gamja=None
    hobak:Hobak=None
    gogi:Gogi=None
    chunjang:Chunjang=None
    myun:Myun=None

class JJajangMyun():
    taste:str = constants.TASTE_GOOD
    type:str = ""
    yangpa:Yangpa=None
    gamja:Gamja=None
    hobak:Hobak=None
    gogi:Gogi=None
    chunjang:Chunjang=None
    myun:Myun=None

    def __init__(self, type):
        if type not in [constants.FOOD_AMOUNT_NORMAL, constants.FOOD_AMOUNT_DOUBLE]:
            raise SBanjumException(f'짜장면 타입이 올바르지 않습니다. type={type}')
        self.type = type

    def get_food(self, myun:Myun, gogi:Gogi, chunjang:Chunjang, yangpa:Yangpa, gamja:Gamja, hobak:Hobak):
        self.myun = myun
        self.chunjang = chunjang
        self.gogi = gogi
        self.yangpa = yangpa
        self.gamja = gamja
        self.hobak = hobak
        if self.type == constants.FOOD_AMOUNT_NORMAL:
            check_value = 1
        elif self.type == constants.FOOD_AMOUNT_DOUBLE:
            check_value = 2
        if myun.amount != recipe.MYUN_AMOUNT*check_value or myun.taste == constants.TASTE_BAD:
            self.taste = constants.TASTE_BAD
        if gogi.amount != recipe.GOGI_AMOUNT*check_value or gogi.taste == constants.TASTE_BAD:
            self.taste = constants.TASTE_BAD
        if chunjang.amount != recipe.CHUNJANG_AMOUNT*check_value or chunjang.taste == constants.TASTE_BAD:
            self.taste = constants.TASTE_BAD
        if yangpa.amount != recipe.YANGPA_AMOUNT*check_value or yangpa.taste == constants.TASTE_BAD:
            self.taste = constants.TASTE_BAD
        if gamja.amount != recipe.GAMJA_AMOUNT*check_value or gamja.taste == constants.TASTE_BAD:
            self.taste = constants.TASTE_BAD
        if hobak.amount != recipe.HOBAK_AMOUNT*check_value or hobak.taste == constants.TASTE_BAD:
            self.taste = constants.TASTE_BAD    