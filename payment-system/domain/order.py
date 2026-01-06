from typing import List
from .money import Money
from .order_status import OrderStatus
from .order_line import OrderLine


class Order:
    def __init__(self, order_id: str):
        self.id = order_id
        self._lines: List[OrderLine] = []
        self.status = OrderStatus.CREATED

    @property
    def lines(self) -> List[OrderLine]:
        return list(self._lines)

    def add_line(self, line: OrderLine):
        if self.status == OrderStatus.PAID:
            raise ValueError("Cannot modify paid order")
        self._lines.append(line)

    def total_amount(self) -> Money:
        total = Money(0)
        for line in self._lines:
            total += line.price
        return total

    def pay(self):
        if not self._lines:
            raise ValueError("Cannot pay empty order")
        if self.status == OrderStatus.PAID:
            raise ValueError("Order already paid")
        self.status = OrderStatus.PAID
