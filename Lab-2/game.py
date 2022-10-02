from base import Base
from field import Field


class Game:
    def __init__(self, field: Field, base: Base):
        self.field = field
        self.base = base

    def render(self):
        self.field.render()

    def is_over(self) -> bool:
        return self.base.is_crushed()
