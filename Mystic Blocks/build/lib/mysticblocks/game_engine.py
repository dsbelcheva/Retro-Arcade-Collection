from .figure import Figure


class MysticBlocks:
    def __init__(self, height, width, mode='default'):
        self.level = 2
        self.score = 0
        self.state = "start"
        self.field = []
        self.height = 0
        self.width = 0
        self.x = 100
        self.y = 60
        self.zoom = 20
        self.figure = None
        self.mode = mode

        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        Figure.figures_generated = 0
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        self.figure = Figure(3, 0)

    def collision(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def remove_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def go_space(self):
        while not self.collision():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.collision():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j +
                                                  self.figure.x] = self.figure.color
                    if self.figure.is_special:
                        for di in (-1, 0, 1):
                            for dj in (-1, 0, 1):
                                ni, nj = i + self.figure.y + di, j + self.figure.x + dj
                                if 0 <= ni < self.height and 0 <= nj < self.width and self.field[ni][nj] > 0:
                                    self.field[ni][nj] = 0
                                    self.score += 50
        self.remove_lines()
        self.new_figure()
        if self.collision():
            self.state = "gameover"

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.collision():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.collision():
            self.figure.rotation = old_rotation
