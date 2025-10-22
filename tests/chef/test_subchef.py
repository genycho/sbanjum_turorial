
#-*- coding: utf-8 -*-
"""
"""
import pytest
from employee.chef import SubChef
# from ingredients.vegetables import Yangpa
# from ingredients.vegetables import Gamja
# from ingredients.vegetables import Hobak
# from ingredients.noodles import Myun
# from ingredients.sauce import Chunjang
# from ingredients.pork_meat import Gogi
from common import sbanjum_constants as constants
# from common.exceptions import CookingException
# from common.exceptions import SBanjumException
from items.foods import FoodItems

def test_subchef_basic():
    """ 테스트 목적 : 알려진 조리법대로 조리 후 맛 확인 """
    test_cook_count = 3

    sub_chef = SubChef("테스트 부주방장")
    result = sub_chef.request_to_cook(cook_count=test_cook_count)
    assert result.chunjang.amount == test_cook_count * 40
    assert result.gamja.amount == test_cook_count * 40
    assert result.gogi.amount == test_cook_count *100
    assert result.hobak.amount == test_cook_count * 40
    # assert result.myun.amount == test_cook_count * 200
    assert result.yangpa.amount == test_cook_count * 100

    assert result.chunjang.taste == constants.TASTE_GOOD
    assert result.gamja.taste == constants.TASTE_GOOD
    assert result.gogi.taste == constants.TASTE_GOOD
    assert result.hobak.taste == constants.TASTE_GOOD
    # assert result.myun.taste == constants.TASTE_GOOD
    assert result.yangpa.taste == constants.TASTE_GOOD
