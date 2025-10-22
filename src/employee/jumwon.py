#-*- coding: utf-8 -*-
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
import common_logger
import fastapi
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from common import sbanjum_constants as constants
from common import menupan
from common.exceptions import SBanjumException
from items.orders import Order
from employee.chef import MainChef

app = FastAPI()
app.common_error_msg = "오류가 발생했습니다. 잠시만 기다려 주세요."
app.logger = common_logger.setup_logger("jumwon")
app.main_chef = MainChef("S셰프")
app.order_dict = {}
app.order_count = 0 

class Item(BaseModel):
    botongCount:Optional[int]
    goppagiCount:Optional[int]

@app.get("/price", description="식사 후 지불할 금액을 확인합니다", status_code=200)
async def get_price(orderId:int):
    """ """
    ur_order = app.order_dict.get(orderId)
    if ur_order == None:
        raise HTTPException(status_code=404, detail=f"주문 내역이 존재하지 않습니다(주문 ID={orderId})")
    try:
        total_price = (ur_order.botong_count * menupan.jjajangmyun_normal) +(ur_order.goppagi_count * menupan.jjajangmyun_double)    
        return _make_response(fastapi.status.HTTP_200_OK, f"전체 가격은 {total_price}원입니다")
    except Exception as detail_chk:
        app.logger.warn(f"Failed!! : {detail_chk.value}")
        raise HTTPException(status_code=500, detail=app.common_error_msg)

@app.post("/order", description="주문하고 음식을 받습니다.", status_code=201) # GET 메소드로 가장 루트 url로 접속할 경우
async def order(item: Item): # root() 함수를 실행하고
    """ 주문하고 가격 확인
    """
    try:
        botong_count = item.botongCount
        goppagi_count = item.goppagiCount
        app.order_count += 1
        order = Order(app.order_count)
        order.set_order(botong_count, goppagi_count)
        app.order_dict[app.order_count] = order
        cooked_food = app.main_chef.request_to_cook(order)
        result_json_dict = {
            "orderId":app.order_count,
            "food":jsonable_encoder(cooked_food)
        }
        return fastapi.responses.JSONResponse(status_code=fastapi.status.HTTP_201_CREATED,content=json.dumps(result_json_dict, ensure_ascii=False),media_type="application/json; charset=utf-8")
    except SBanjumException as chef_saying:
        app.logger.warn(f"Failed!! : {chef_saying.value}")
        raise HTTPException(status_code=500, detail=str(chef_saying.value))
    except Exception as detail_chk:
        app.logger.warn(f"Failed!! : {detail_chk.value}")
        raise HTTPException(status_code=500, detail=app.common_error_msg)

def _make_200_response(body_text):
    return _make_response(fastapi.status.HTTP_200_OK, body_text)

def _make_response(status_code, body_text):
    return fastapi.responses.JSONResponse(
        status_code=status_code,
        content={"result" : body_text},
        headers={"content-type": "application/json"}
    )