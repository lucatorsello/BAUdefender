from entity.entity import Entity


class EnemyEntity(Entity):
    def __init__(self, speed: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = speed

    def move(self):
        print((self.window.get_width() // 2))
        print(self.y_pos)
        if self.x_pos != (self.window.get_width() // 2):
            direction = -1 if self.x_pos > (self.window.get_width() // 2) else 1
            self.x_pos += direction * self.speed
        if self.y_pos != (self.window.get_height() // 2):
            direction = -1 if self.y_pos > (self.window.get_height() // 2) else 1
            self.y_pos += direction * self.speed
