from Interfaces.order_repository import OrderRepository


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._orders = {}

    def get_by_id(self, order_id: str):
        return self._orders[order_id]

    def save(self, order):
        self._orders[order.id] = order
