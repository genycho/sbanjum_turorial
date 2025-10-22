#-*- coding: utf-8 -*-
import time
from common.exceptions import SBanjumException, CookingException
from common import sbanjum_constants as constants
import common_logger
from items.orders import Order
from queue import Queue
from items.foods import JJajangMyun
from items.foods import FoodItems
from ingredients.vegetables import Yangpa
from ingredients.vegetables import Gamja
from ingredients.vegetables import Hobak
from ingredients.noodles import Myun
from ingredients.sauce import Chunjang
from ingredients.pork_meat import Gogi  

class Chef():
    """ 주방장 기본 클래스입니다."""
    name:str = ''
    role:str = ''
    __salary:float = 0.0
    logger = None

    def __init__(self, name):
        self.name = name
        self.logger = common_logger.setup_logger(self.__class__.__name__)

    def set_role(self, role):
        self.role = role

    def __str__(self):
        return f'[Details] name={self.name}, role={self.role}'
    

class ChoboChef(Chef):
    """ 초보 주방장입니다."""
    var_cook_timeseconds = constants.COOKTIME_CHOBOCHEF_SECONDS  # 요리하는데 걸리는 시간(초)
    yangpa:Yangpa=None
    gamja:Gamja=None
    hobak:Hobak=None

    def __init__(self, name):
        super().__init__(name)
        self.set_role(constants.ROLE_CHOBOCHEF)

    def request_to_cook(self, cook_count:int):
        self.logger.info(f'초보주방장 채소 재료 준비합니다. {cook_count}인분 준비!')
        self.yangpa = Yangpa(100 * cook_count)
        self.yangpa.slice(constants.SIZE_MEDIUM)
        self.gamja = Gamja(40 * cook_count)
        self.gamja.slice(constants.SIZE_MEDIUM)
        self.hobak = Hobak(40 * cook_count)
        self.hobak.slice(constants.SIZE_MEDIUM)
        time.sleep(self.var_cook_timeseconds)
        self.logger.info(f'재료 준비 끝났습니다 {cook_count}인분 준비!')

class SubChef(Chef):
    """ 부주방장입니다."""
    var_cook_timeseconds = constants.COOKTIME_SUBCHEF_SECONDS  # 요리하는데 걸리는 시간(초)
    chobo_chef = ChoboChef('S초보주방장')

    def __init__(self, name):
        super().__init__(name)
        self.set_role(constants.ROLE_SUBCHEF)

    def request_to_cook(self, cook_count:int):
        self.logger.info(f'부주방장 요리 시작합니다. {cook_count}인분 준비!')
        self.logger.info(f'초보주방장, {cook_count} 재료 준비해 주세요.')
        self.chobo_chef.request_to_cook(cook_count)
        # THINKME: 초보 주방장이 일을 제대로 했는지 매번 확인할 것인가? vs 믿고 다음으로 진행할 것인가?
        food_items = FoodItems()
        ## INJECTED 
        # gamja = self.chobo_chef.gamja.cook(120)
        # yangpa = self.chobo_chef.yangpa.cook(120)
        # hobak = self.chobo_chef.hobak.cook(120)
        gamja = self.chobo_chef.gamja   # INJECTED 감자, 호박을 겹쳐서 설정. 
        gamja.cook(120)
        yangpa = self.chobo_chef.yangpa
        yangpa.cook(120)
        hobak = self.chobo_chef.hobak
        hobak.cook(120)
        gogi = Gogi(100 * cook_count)
        gogi.cook(240)
        chunjang = Chunjang(40 * cook_count)
        chunjang.cook(120)
        ## 재료 모두 합쳐 끓이기
        food_items.yangpa = yangpa
        food_items.gamja = gamja
        food_items.hobak = hobak
        food_items.gogi = gogi
        food_items.chunjang = chunjang
        return food_items
    
class MainChef(Chef):
    """ 주방을 책임지는 메인 주방장입니다."""
    var_max_order_count = 10
    var_cook_timeseconds = constants.COOKTIME_MAINCHEF_SECONDS  # 요리하는데 걸리는 시간(초)
    to_cook_list:list = []
    finished_order_list:list = []
    sub_chef = SubChef('S부주방장')

    def __init__(self, name):
        super().__init__(name)
        self.set_role(constants.ROLE_MAINCHEF)

    def request_to_cook(self, order:Order) -> list:
        if len(self.to_cook_list) > self.var_max_order_count:
            raise SBanjumException('요리 대기열이 꽉 찼습니다. 더 주문을 받을 수 없습니다.')
        self.to_cook_list.append(order)
        cur_order:Order = self.to_cook_list.pop(0)
        self.logger.info(f'요리 시작합니다. {cur_order}')
        # cook_count = order.botong_count + (order.goppagi_count * 2)   #INJECTED   
        cook_count = (cur_order.botong_count*2) + cur_order.goppagi_count
        self.logger.info(f'부주방장, {cook_count}인분 준비해 주세요.')
        food_items = self.sub_chef.request_to_cook(cook_count)
        myun = Myun(200 * cook_count)
        myun.cook(300)
        food_items.myun = myun

        food_list = []
        for _ in range(cur_order.botong_count):
            time.sleep(self.var_cook_timeseconds)
            jajangMyun = JJajangMyun("보통")
            # jajangMyun.get_food(food_items.myun.have_amount(200), food_items.chunjang.have_amount(40), food_items.gogi.have_amount(100), food_items.yangpa.have_amount(100), food_items.gamja.have_amount(40), food_items.hobak.have_amount(40))  #INJECTED 순서가 바뀌어서 들어감
            jajangMyun.get_food(food_items.myun.have_amount(200), food_items.gogi.have_amount(100), food_items.chunjang.have_amount(40), food_items.yangpa.have_amount(100), food_items.gamja.have_amount(40), food_items.hobak.have_amount(40))
            food_list.append(jajangMyun)
        
        for _ in range(cur_order.goppagi_count):
            time.sleep(self.var_cook_timeseconds)
            jajangMyun = JJajangMyun("곱빼기")
            jajangMyun.get_food(food_items.myun.have_amount(400), food_items.gogi.have_amount(200), food_items.chunjang.have_amount(80), food_items.yangpa.have_amount(200), food_items.gamja.have_amount(80), food_items.hobak.have_amount(80))
            food_list.append(jajangMyun)
        return food_list
