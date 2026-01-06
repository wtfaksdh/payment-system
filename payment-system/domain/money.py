from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    amount: int
    currency: str = "RUB"

    def __add__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Currency mismatch")
        return Money(self.amount + other.amount, self.currency)
