from object import Object


class Field:
    def __init__(self, width: int, height: int, max_objects: int, objects: list[Object]):
        self.width = width
        self.height = height
        self.max_objects = max_objects
        self.objects = objects


"""

init_objects = [bushes, units, ]
init_field   = Field(100, 100, )

"""
