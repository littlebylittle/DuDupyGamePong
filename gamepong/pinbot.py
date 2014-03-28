from pinplatform import Pin


class Pinbot(Pin):
    # def __init__(self, surface, x_pos):
    #
    #     super(Pinbot, self).__init__(self, surface, x_pos)
    #     pass
    def register_ball(self, ball):
        self.ball = ball

    def follow_ball(self):
        self.rect.y = self.ball.rect.y

    pass