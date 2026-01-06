import pytest

from domain.order import Order
from domain.order_line import OrderLine
from domain.money import Money
from application.pay_order_use_case import PayOrderUseCase
from infrastructure.in_memory_order_repository import InMemoryOrderRepository
from infrastructure.fake_payment_gateway import FakePaymentGateway


def create_use_case(order):
    repo = InMemoryOrderRepository()
    repo.save(order)
    gateway = FakePaymentGateway()
    return PayOrderUseCase(repo, gateway), repo


def test_successful_payment():
    order = Order("1")
    order.add_line(OrderLine("Book", Money(100)))

    uc, repo = create_use_case(order)
    uc.execute("1")

    assert repo.get_by_id("1").status.name == "PAID"


def test_empty_order_payment_error():
    order = Order("2")
    uc, _ = create_use_case(order)

    with pytest.raises(ValueError):
        uc.execute("2")


def test_double_payment_error():
    order = Order("3")
    order.add_line(OrderLine("Pen", Money(50)))

    uc, _ = create_use_case(order)
    uc.execute("3")

    with pytest.raises(ValueError):
        uc.execute("3")


def test_cannot_modify_paid_order():
    order = Order("4")
    order.add_line(OrderLine("Notebook", Money(200)))

    uc, _ = create_use_case(order)
    uc.execute("4")

    with pytest.raises(ValueError):
        order.add_line(OrderLine("Pencil", Money(10)))


def test_total_amount_calculation():
    order = Order("5")
    order.add_line(OrderLine("A", Money(100)))
    order.add_line(OrderLine("B", Money(200)))

    assert order.total_amount().amount == 300
