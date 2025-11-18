
#-*- coding: utf-8 -*-
import pytest
from employee.chef import SubChef, ChoboChef
from ingredients.vegetables import Yangpa
from ingredients.vegetables import Gamja
from ingredients.vegetables import Hobak
from common import sbanjum_constants as constants
# from common.exceptions import CookingException
# from common.exceptions import SBanjumException
from items.foods import FoodItems

def test_subchef_nochasoe_hobak(mocker):
    """ 테스트 목적 : 초보주방장이 재료를 빠뜨렸을 때 """
    mock_chobo_chef = ChoboChef("임시 초보 주방장")
    mock_chobo_chef.yangpa = Yangpa(100)
    mock_chobo_chef.gamja = Gamja(40)   
    mock_chobo_chef.hobak = None
    mocker.patch.object(SubChef, "chobo_chef", mock_chobo_chef)
    mocker.patch("employee.chef.ChoboChef.request_to_cook",return_value=None)
    
    test_cook_count = 1
    sub_chef = SubChef("테스트 부주방장")
    with pytest.raises(Exception) as details:
        result = sub_chef.request_to_cook(cook_count=test_cook_count)
    assert "초보야! 일 똑바로 안할래?!" == details.value.args[0]

def test_subchef_wrongamountchasoe(mocker):
    """ 테스트 목적 : 양을 잘못 준비했을 때 """
    mock_chobo_chef = ChoboChef("임시 초보 주방장")
    mock_chobo_chef.yangpa = Yangpa(120)
    mock_chobo_chef.gamja = Gamja(100)   
    mock_chobo_chef.hobak = Hobak(80)
    mocker.patch.object(SubChef, "chobo_chef", mock_chobo_chef)
    mocker.patch("employee.chef.ChoboChef.request_to_cook")
    
    test_cook_count = 1
    sub_chef = SubChef("테스트 부주방장")
    with pytest.raises(Exception) as details:
        result = sub_chef.request_to_cook(cook_count=test_cook_count)
    assert "초보야! 일 똑바로 안할래?!" == details.value.args[0]
    # pytest.fail("Not yet implemented")

def test_subchef_notslicedchasoe(mocker):
    """ 테스트 목적 : 초보주방장이 안 썰었을 때 """
    mock_chobo_chef = ChoboChef("임시 초보 주방장")
    mock_chobo_chef.yangpa = Yangpa(100)
    mock_chobo_chef.gamja = Gamja(40)   
    mock_chobo_chef.hobak = Hobak(40)
    mocker.patch.object(SubChef, "chobo_chef", mock_chobo_chef)
    mocker.patch("employee.chef.ChoboChef.request_to_cook")
    
    test_cook_count = 1
    sub_chef = SubChef("테스트 부주방장")
    with pytest.raises(Exception) as details:
        result = sub_chef.request_to_cook(cook_count=test_cook_count)
    assert "초보야! 일 똑바로 안할래?!" == details.value.args[0]



