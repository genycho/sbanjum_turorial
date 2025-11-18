from employee.chef import MainChef
from items.orders import Order

def create_order(botong_count=1, goppagi_count=0):
    """
    Robot Framework에서 사용할 Order 생성 함수
    """
    return Order(botong_count=int(botong_count), goppagi_count=int(goppagi_count))

def create_main_chef(name):
    """
    메인 주방장 객체 생성
    """
    chef = MainChef(name)
    return chef

def main_chef_request_to_cook(chef, order):
    """
    MainChef.request_to_cook 래핑
    """
    return chef.request_to_cook(order)
