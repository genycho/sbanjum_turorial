#-*- coding: utf-8 -*-
import copy
from common.exceptions import CookingException
from common import sbanjum_constants as constants
from abc import ABC, abstractmethod

class Jaeryo(ABC):
    """ 재료이름, 상태, 맛, 몇인분용 재료양
    """
    name : str = ''
    status : str = constants.JAERYO_STATUS_INIT
    taste : str = constants.TASTE_BAD
    amount: float = 0.0
	
    def __init__(self, name, amount=0.0):
        self.name = name
        self.status = constants.JAERYO_STATUS_INIT
        self.amount = amount

    def __str__(self):
        return f'[Details] name={self.name}, status={self.status}, taste={self.taste}, amount={self.amount}'

    @abstractmethod
    def cook(self, cook_seconds):
        pass

    def have_amount(self, to_have_amount):
        if (self.amount - to_have_amount) <0:
            raise CookingException(f'재료 양이 부족합니다. 현재 재료양={self.amount}, 요청 재료양={to_have_amount}')
        self.amount -= to_have_amount
        to_return = copy.deepcopy(self)
        to_return.amount = to_have_amount
        return to_return

class Chaeso(Jaeryo):
    """ 재료이름, 상태, 맛, 몇인분용 재료양
    """
    sliced_size : str = ''

    @abstractmethod
    def cook(self, cook_seconds):
        pass

    def cut(self, amount):
        self.set_amount(amount)

    def slice(self, size):
        self.sliced_size = size
        # self.status == constants.JAERYO_STATUS_SLICED    #INJECTED. 실제 코드 결함 사례
        self.status = constants.JAERYO_STATUS_SLICED