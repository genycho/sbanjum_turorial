
#-*- coding: utf-8 -*-
""" 양파를 어떻게 조리해야 가장 맛있는지 확인하는 테스트 """
import pytest
from ingredients.vegetables import Yangpa
from common import sbanjum_constants as constants
from common.exceptions import CookingException
from common.exceptions import SBanjumException


def test_yangpa_basic():
    """ 테스트 목적 : 알려진 조리법대로 조리 후 맛 확인 """
    amount = 100
    cook_seconds = 120
    slice_size = constants.SIZE_MEDIUM

    yangpa = Yangpa(amount)	
    yangpa.slice(slice_size)
    yangpa.cook(cook_seconds)

    assert '양파' == yangpa.name
    assert 0.25 == yangpa.amount
    assert constants.JAERYO_STATUS_FRIED == yangpa.status
    assert constants.TASTE_GOOD == yangpa.taste
	
def test_yangpa_morethan120s():
    """ 테스트 목적 : 120초 이상으로 볶았을 때 """
    amount = 100
    cook_seconds = 180  #3분
    slice_size = constants.SIZE_MEDIUM

    yangpa = Yangpa(amount)	
    yangpa.slice(slice_size)
    yangpa.cook(cook_seconds)

    assert constants.TASTE_GOOD == yangpa.taste
	
def test_yangpa_lessthan120s():
    """ 테스트 목적 :알려진 조리법대로 조리 후 맛 확인 """
    amount = 100
    cook_seconds = 90   #1분30초
    slice_size = constants.SIZE_MEDIUM

    yangpa = Yangpa(amount)			
    yangpa.slice(slice_size)
    yangpa.cook(cook_seconds)

    assert constants.TASTE_GOOD == yangpa.taste
	

def test_yangpa_nocook():
    """ 테스트 목적 : 썰기만 하고 볶지 않은 상태로 맛보기 """
    amount = 100
    slice_size = constants.SIZE_MEDIUM

    yangpa = Yangpa(amount)			
    yangpa.slice(slice_size)
    # yangpa.cook(cook_seconds) #INJECTED
    assert constants.TASTE_BAD == yangpa.taste
    assert constants.JAERYO_STATUS_FRIED == yangpa.status

def test_yangpa_cooktoolong():
    """ 테스트 목적 : 10분이상으로 과하게 오래 볶았을 때 문제 상황 확인 """
    amount = 100
    cook_seconds = 600  #10분
    slice_size = constants.SIZE_MEDIUM

    yangpa = Yangpa(amount)			
    yangpa.slice(slice_size)
    yangpa.cook(cook_seconds)

    assert constants.JAERYO_STATUS_FRIED == yangpa.status
    assert constants.TASTE_BAD == yangpa.taste
    #THINKME    화재 위험도 있으니 Exception 을 발생시켜야 하지는 않을까???
	
def test_yangpa_wrongamount():
    """ 테스트 목적: 알려진 조리법대로 조리 후 맛 확인 """
    amount = 200
    cook_seconds = 120
    slice_size = constants.SIZE_MEDIUM

    yangpa = Yangpa(amount)			
    yangpa.slice(slice_size)
    yangpa.cook(cook_seconds)

    assert '양파' == yangpa.name
    assert 0.25 == yangpa.amount
    # assert 0.25 == yangpa.amount  #FIXME
    assert constants.JAERYO_STATUS_FRIED == yangpa.status
    assert constants.TASTE_GOOD == yangpa.taste
	
def test_yangpa_wrongsilcesize():
    """ 테스트 목적: 중간 크기가 아닌 사이즈로 썰은 후 볶았을 때 맛 확인"""
    amount = 100
    cook_seconds = 120
    slice_size = constants.SIZE_LARGE
		
    yangpa = Yangpa(amount)	
    yangpa.slice(slice_size)
    yangpa.cook(cook_seconds)

    assert '양파' == yangpa.name
    assert 0.25 == yangpa.amount
    assert constants.JAERYO_STATUS_FRIED == yangpa.status
    assert constants.TASTE_GOOD == yangpa.taste #FIXME
    # assert constants.TASTE_BAD == yangpa.taste    #FIXME
	
def test_yangpa_slicingskipped():
    """ 테스트 목적: 썰지 않고 바로 볶았을 때 """
    amount = 100
    cook_seconds = 120
    # slice_size = constants.SIZE_MEDIUM    #INJECTED
    
    yangpa = Yangpa(amount)	
    # yangpa.slice(slice_size)  #INJECTED
    yangpa.cook(cook_seconds)

    assert constants.JAERYO_STATUS_FRIED == yangpa.status
    assert constants.TASTE_BAD == yangpa.taste

############ Grey-box Test Cases ############
def test_yangpa_cooktimezero():
    """ 테스트 목적: 0초로 볶기 시도했을 때 for Exception 발생 확인 테스트 실습"""
    amount = 100
    cook_seconds = 0
    slice_size = constants.SIZE_MEDIUM

    # with pytest.raises(CookingException) as details:  #FIXME
    with pytest.raises(SBanjumException) as details:    #FIXME
        yangpa = Yangpa(amount)	
        yangpa.slice(slice_size)
        yangpa.cook(cook_seconds)
    assert '0초 이상을 조리해 주세요.' == str(details.value)

@pytest.mark.parametrize("cook_seconds, expect_taste", [(109,constants.TASTE_BAD), (110,constants.TASTE_GOOD), (130,constants.TASTE_BAD)])
def test_yangpa_cooktime110s(cook_seconds, expect_taste):
    """ 테스트 목적: 110초 아상, 130초 미만인 경계조건에 대한 테스트, pytest의 parametrize 활용 """
    amount = 100
    slice_size = constants.SIZE_MEDIUM

    yangpa = Yangpa(amount)	
    yangpa.slice(slice_size)
    yangpa.cook(cook_seconds)
    assert expect_taste == yangpa.taste

def test_yangpa_slicesizesmall():
    """ 테스트 목적: test_썰기크기에대한추가테스트 """
    amount = 100
    cook_seconds = 120
    slice_size = constants.SIZE_SMALL
		
    yangpa = Yangpa(amount)	
    yangpa.slice(slice_size)
    yangpa.cook(cook_seconds)

    assert constants.TASTE_GOOD == yangpa.taste #FIXME
    # assert constants.TASTE_BAD == yangpa.taste  #FIXME

def test_yangpa_copyyangpa():
    """ 테스트 목적: test_썰기크기에대한추가테스트 """
    amount = 100
    cook_seconds = 180  #3분
    slice_size = constants.SIZE_MEDIUM

    yangpa = Yangpa(amount)	
    yangpa.slice(slice_size)
    yangpa.cook(cook_seconds)
    # assert constants.TASTE_GOOD == yangpa.taste
    new_yangpa = yangpa.have_amount(25)
    # assert constants.TASTE_GOOD == new_yangpa.taste
    assert 25 == new_yangpa.amount
    assert constants.JAERYO_STATUS_FRIED == new_yangpa.status

