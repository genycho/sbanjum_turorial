#-*- coding: utf-8 -*-
from common.exceptions import CookingException
from common import sbanjum_constants as constants
from abc import ABC, abstractmethod

class Order():
    order_id : int = 0
    botong_count : int = 0
    goppagi_count : int = 0

    def __init__(self, order_no:int):
        self.order_id = order_no

    def set_order(self, botong_count:int, goppagi_count:int):
        self.botong_count = botong_count
        self.goppagi_count = goppagi_count  
        
    def __str__(self):
        return f'[Order] order_id={self.order_id}, botong_count={self.botong_count}, goppagi_count={self.goppagi_count}'