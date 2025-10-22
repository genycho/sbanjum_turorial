
#-*- coding: utf-8 -*-
"""  """
import pytest
from employee.chef import MainChef
from items.orders import Order
from ingredients.vegetables import Yangpa
from ingredients.vegetables import Gamja
from ingredients.vegetables import Hobak
from ingredients.noodles import Myun
from ingredients.sauce import Chunjang
from ingredients.pork_meat import Gogi
from common import sbanjum_constants as constants
from common.exceptions import CookingException
from common.exceptions import SBanjumException
from items.foods import JJajangMyun
from items.foods import FoodItems

def _get_food_items():
    mock_food_items = FoodItems()
    mock_food_items.chunjang = Chunjang(40)
    mock_food_items.gogi = Gogi(100)
    mock_food_items.yangpa = Yangpa(100)
    mock_food_items.gamja = Gamja(40)
    mock_food_items.hobak = Hobak(40)
    mock_food_items.myun = Myun(200)
    mock_food_items.yangpa.taste = constants.TASTE_GOOD
    mock_food_items.gamja.taste = constants.TASTE_GOOD
    mock_food_items.hobak.taste = constants.TASTE_GOOD
    return mock_food_items

def test_mainchef_notenoughamount(mocker):
    """ 테스트 목적 : 주방장이 재료 양이 부족할 때 예외처리하는지 확인
    """
    mock_food_items = _get_food_items()
    # mocker.spy(calculator_machine, "multiply")
    mocker.patch("employee.chef.SubChef.request_to_cook", return_value=mock_food_items)

    main_chef = MainChef("메인주방장")
    order = Order(1)
    order.set_order(botong_count=2,goppagi_count=1)   # 총 4인분
    with pytest.raises(CookingException) as excinfo:
        main_chef.request_to_cook(order)
    assert str(excinfo.value) == "재료 양이 부족합니다. 현재 재료양=0, 요청 재료양=100"

def test_mainchef_badtaste(mocker):
    """ 테스트 목적 : 주방장이 재료 맛이 안좋을 때 예외처리하는지 확인
    """
    cook_count = 4
    mock_food_items = _get_food_items()
    mock_food_items.yangpa.amount = 100 * cook_count
    mock_food_items.gamja.amount = 40 * cook_count
    mock_food_items.hobak.amount = 40 * cook_count
    mock_food_items.myun.amount = 200 * cook_count
    mock_food_items.gogi.amount = 100 * cook_count
    mock_food_items.chunjang.amount = 40 * cook_count
    mocker.patch("employee.chef.SubChef.request_to_cook", return_value=mock_food_items)

    main_chef = MainChef("메인주방장")
    order = Order(1)
    order.set_order(botong_count=2,goppagi_count=1)   # 총 5인분 (2*2 + 1)
    result = main_chef.request_to_cook(order)

    # Assert
    assert len(result) ==3

def test_mainchef_exceptions(mocker):
    """ 테스트 목적 : 주방장이 재료 맛이 안좋을 때 예외처리하는지 확인
    """
    mock_food_items = _get_food_items()
    # mocker.patch("employee.chef.SubChef.request_to_cook", return_value=mock_food_items)
    mocker.patch("employee.chef.SubChef.request_to_cook", side_effect=SBanjumException("주방장님 재료가 다 탔어요"))

    main_chef = MainChef("메인주방장")
    order = Order(1)
    order.set_order(botong_count=1,goppagi_count=0)   # 총 5인분 (2*2 + 1)
    result = main_chef.request_to_cook(order)

    # Assert
    assert len(result) ==3