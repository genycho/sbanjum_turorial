#-*- coding: utf-8 -*-
"""
"""
import pytest
from employee.chef import ChoboChef
from ingredients.vegetables import Yangpa
# from ingredients.vegetables import Gamja
# from ingredients.vegetables import Hobak
# from ingredients.noodles import Myun
# from ingredients.sauce import Chunjang
# from ingredients.pork_meat import Gogi
from common import sbanjum_constants as constants
# from common.exceptions import CookingException
# from common.exceptions import SBanjumException
from items.foods import FoodItems

def test_chobochef_basic():
    """ 테스트 목적 : 알려진 조리법대로 조리 후 맛 확인 """
    test_cook_count = 3

    chobo_chef = ChoboChef("테스트 초보 주방장")
    chobo_chef.request_to_cook(cook_count=test_cook_count)
    assert chobo_chef.gamja.amount == test_cook_count * 40
    assert chobo_chef.hobak.amount == test_cook_count * 40
    assert chobo_chef.yangpa.amount == test_cook_count * 100

    assert chobo_chef.gamja.status == constants.JAERYO_STATUS_SLICED
    assert chobo_chef.hobak.status == constants.JAERYO_STATUS_SLICED
    assert chobo_chef.yangpa.status == constants.JAERYO_STATUS_SLICED

    assert chobo_chef.gamja.sliced_size == constants.SIZE_MEDIUM
    assert chobo_chef.hobak.sliced_size == constants.SIZE_MEDIUM
    assert chobo_chef.yangpa.sliced_size == constants.SIZE_MEDIUM

    assert chobo_chef.gamja.taste == constants.TASTE_BAD
    assert chobo_chef.hobak.taste == constants.TASTE_BAD
    assert chobo_chef.yangpa.taste == constants.TASTE_BAD

def test_chobochef_0inbun():
    """ 테스트 목적 : 0인분에 대한 처리 테스트 """
    test_cook_count = 0

    chobo_chef = ChoboChef("테스트 초보 주방장")
    with pytest.raises(Exception) as details:
        chobo_chef.request_to_cook(cook_count=test_cook_count)
    assert "" == details.value.args[0]

@pytest.mark.skip(reason="pytest-mock 적용이 필요")
def test_chobochef_rottenchasoe():
    """ 테스트 목적 : 채소가 상해 있을 때 처리 확인 """
    pytest.fail("Not yet implemented")


  
