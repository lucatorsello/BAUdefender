from entity.entity import Entity


class EnemyEntity(Entity):
    def __init__(self, speed: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = speed
        self.target_pos = (self.window.get_width() // 2, self.window.get_height() // 2)

    def auto_move(self, enemy_list: list):
        if self.x_pos != self.target_pos[0]:
            x_direction = -1 if self.x_pos > self.target_pos[0] else 1
            new_x_pos = self.x_pos + (x_direction * self.speed)
            if not self.check_collision_with_entities(
                enemy_list, new_x_pos, self.y_pos
            ):
                self.x_pos = self.x_pos + x_direction * self.speed
            # else:
            #     self.x_pos = self.x_pos - x_direction * self.speed

        if self.y_pos != self.target_pos[1]:
            y_direction = -1 if self.y_pos > self.target_pos[1] else 1
            new_y_pos = self.y_pos + (y_direction * self.speed)
            if not self.check_collision_with_entities(
                enemy_list, self.x_pos, new_y_pos
            ):
                self.y_pos = self.y_pos + y_direction * self.speed
            # else:
            #     self.y_pos = self.y_pos - y_direction * self.speed
