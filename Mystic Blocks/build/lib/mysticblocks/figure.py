import random

colors = [
    (0, 0, 0),  # BLACK
    (120, 37, 179),  # PURPLE
    (100, 179, 179),  # LIGHT_BLUE
    (80, 34, 22),  # BROWN
    (80, 134, 22),  # GREEN
    (180, 34, 22),  # RED
    (180, 34, 122),  # PINK
    (255, 215, 0),  # GOLD FOR SPECIAL BLOCKS
]


class Figure:
    x = 0
    y = 0
    figures_generated = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],  # "I"
        [[4, 5, 9, 10], [2, 6, 5, 9]],  # "S"
        [[6, 7, 9, 10], [1, 5, 6, 10]],  # "Z"
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],  # "T"
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  # "L"
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # "J"
        [[1, 2, 5, 6]],  # "O"
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        Figure.figures_generated += 1
        if Figure.figures_generated % 5 == 0:
            self.is_special = True
            self.color = len(colors) - 1
        else:
            self.is_special = False
            self.color = random.randint(1, len(colors) - 2)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
