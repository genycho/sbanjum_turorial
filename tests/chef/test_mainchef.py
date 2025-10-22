
#-*- coding: utf-8 -*-
""" 
"""
import pytest
from ingredients.vegetables import Yangpa
from common import sbanjum_constants as constants
from common.exceptions import CookingException
from common.exceptions import SBanjumException
from items.orders import Order
from employee.chef import MainChef

@pytest.fixture(scope='function')
def main_chef():
    return MainChef("테스트 세프")

def test_mainchef_basic(main_chef):
    """ 테스트 목적 : 알려진 조리법대로 조리 후 맛 확인 """
    test_order:Order = Order(1)
    test_order.set_order(botong_count=1, goppagi_count=1)

    food_list = main_chef.request_to_cook(test_order)
    assert 2 == len(food_list)
    first_food = food_list[0]
    assert constants.TASTE_GOOD == first_food.taste
    assert first_food.type == constants.FOOD_AMOUNT_NORMAL
    assert first_food.myun.amount == 200
    second_food = food_list[1]
    assert constants.TASTE_GOOD == second_food.taste
    assert second_food.type == constants.FOOD_AMOUNT_DOUBLE
    assert second_food.myun.amount == 400

def test_mainchef_onetypeonly(main_chef):
    """ 테스트 목적 : 보통, 곱빼기 한 종류만 주문 """
    test_order:Order = Order(1)
    test_order.set_order(botong_count=5, goppagi_count=0)

    food_list = main_chef.request_to_cook(test_order)
    assert 5 == len(food_list)
    first_food = food_list[0]
    assert first_food.type == constants.FOOD_AMOUNT_NORMAL

    test_order.set_order(botong_count=0, goppagi_count=3)
    food_list = main_chef.request_to_cook(test_order)
    assert 3 == len(food_list)
    
def test_mainchef_morethan10orders(main_chef):
    """ 테스트 목적 : 주문 10개 초과 주문 시 예외처리 """
    order_id = 0
    for i in range(10):
        order_id += 1
        test_order:Order = Order(order_id)
        test_order.set_order(botong_count=1, goppagi_count=0)
        food_list = main_chef.request_to_cook(test_order)
        assert 1 == len(food_list)
    #  11번째 주문
    order_id += 1
    test_order:Order = Order(order_id)
    with pytest.raises(SBanjumException) as excinfo:
        test_order.set_order(botong_count=1, goppagi_count=0)
    assert str(excinfo.value) == "요리 대기열이 꽉 찼습니다. 더 주문을 받을 수 없습니다."
    