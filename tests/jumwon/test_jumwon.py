#-*- coding: utf-8 -*-
"""
"""
import pytest
from fastapi.testclient import TestClient
from employee.jumwon import app

client = TestClient(app)

def test_jumwon_askprice_basic():
    """ 테스트 목적 : 가격 확인 """
    response = client.get("/price", params = {"orderId":1})
    assert 200 == response.status_code, response.text
    response_body = response.json()
    assert 'result' in response_body
    assert '카페라떼는 5000 원입니다' == response_body['result']

def test_jumwon_order_basic():
    """ 테스트 목적 : 기본 주문 확인 """
    data = {
        "botongCount" : 1,
        "goppagiCount" : 1
    }
    response = client.post("/order", json = data)
    assert 201 == response.status_code, response.text
    response_body = response.json()
    assert 'result' in response_body
    assert '전체 가격은 9000원입니다' == response_body['result']