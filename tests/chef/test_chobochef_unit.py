#-*- coding: utf-8 -*-
"""
"""
import pytest
from employee.chef import ChoboChef
from ingredients.vegetables import Yangpa
from common import sbanjum_constants as constants
# from common.exceptions import CookingException
# from common.exceptions import SBanjumException
from items.foods import FoodItems

def test_chobochef_rottenchasoe(mocker):
    """ 테스트 목적 : 채소(양파)가 상해 있을 때 처리 확인 """
    mock_yangpa = Yangpa(100)
    mock_yangpa.status = constants.JAERYO_STATUS_ROTTEN
    mock_yangpa.slice = mocker.Mock()  # 호출되더라도 아무 동작 안 하게
    mocker.patch("employee.chef.Yangpa", return_value=mock_yangpa)  #chef.py에 import된 Yangpa를 대체

    chobo_chef = ChoboChef("테스트 초보 주방장")
    with pytest.raises(Exception) as details:
        chobo_chef.request_to_cook(cook_count=1)
    assert "양파가 상했는데 어떡하죠?" in str(details.value)
    # assert chobo_chef.yangpa is mock_yangpa



  
