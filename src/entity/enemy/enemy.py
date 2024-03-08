from entity.entity import Entity


class EnemyEntity(Entity):
    def __init__(self, speed: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = speed

    def move(self, enemy_list: list):
        center_x = self.window.get_width() // 2
        center_y = self.window.get_height() // 2

        if self.x_pos != center_x:
            x_direction = -1 if self.x_pos > center_x else 1
            new_x_pos = self.x_pos + x_direction * self.speed
            if not self.check_collision_with_entities(
                enemy_list, new_x_pos, self.y_pos
            ):
                self.x_pos = self.x_pos + x_direction * self.speed
            # else:
            #     self.x_pos = self.x_pos - x_direction * self.speed

        if self.y_pos != center_y:
            y_direction = -1 if self.y_pos > center_y else 1
            new_y_pos = self.y_pos + y_direction * self.speed
            if not self.check_collision_with_entities(
                enemy_list, self.x_pos, new_y_pos
            ):
                self.y_pos = self.y_pos + y_direction * self.speed
            # else:
            #     self.y_pos = self.y_pos - y_direction * self.speed
