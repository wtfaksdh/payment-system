# Lab7TP

## Описание проекта

Реализация системы оплаты заказов с использованием **многослойной архитектуры** и принципов **DDD-lite (Domain-Driven Design)**.  
Проект демонстрирует **разделение ответственности между слоями** и **инкапсуляцию бизнес-логики в доменном слое**.

---

## Структура проекта (слоистая архитектура)

### Доменный слой (Domain)  
**Расположение:** `src/domain/`

- `order.py` — сущность `Order` (агрегат)  
- `order_line.py` — часть агрегата `OrderLine`  
- `money.py` — Value Object `Money`  
- `order_status.py` — статусы заказа (`CREATED`, `PAID`)  

> В доменном слое реализованы **инварианты**:  
> - нельзя оплатить пустой заказ  
> - нельзя оплатить заказ повторно  
> - после оплаты нельзя менять строки заказа  
> - итоговая сумма = сумма строк заказа

---

### Слой приложения (Application)  
**Расположение:** `src/application/`

- `pay_order_use_case.py` — Use Case `PayOrderUseCase`  
  (загрузка заказа, оплата, вызов платежного шлюза, сохранение заказа, возврат результата)

---

### Интерфейсы (Interfaces)  
**Расположение:** `src/interfaces/`

- `order_repository.py` — `OrderRepository` (интерфейс)  
- `payment_gateway.py` — `PaymentGateway` (интерфейс)  

> Use-case зависит только от этих интерфейсов, что обеспечивает соблюдение **DIP**.

---

### Инфраструктурный слой (Infrastructure)  
**Расположение:** `src/infrastructure/`

- `in_memory_order_repository.py` — `InMemoryOrderRepository` (реализация `OrderRepository`)  
- `fake_payment_gateway.py` — `FakePaymentGateway` (реализация `PaymentGateway`)  

> Реальная база данных и реальный шлюз оплаты не используются.

---

### Тесты  
**Расположение:** `tests/`

- `test_pay_order.py` — тесты всех сценариев:
