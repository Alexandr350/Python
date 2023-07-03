from Utils import randcell
import os


class Helicopter:
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.h = h
        self.w = w
        self.y = ry
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.lives = 2000

    def move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y
        if 0 <= nx < self.h and 0 <= ny < self.w:
            self.x, self.y = nx, ny

    def print_menu(self):
        print("🧯 ", self.tank, "/", self.mxtank, sep='', end=" | ")
        print("🏆", self.score, end=" | ")
        print("💛", self.lives)

    def game_over(self):
        os.system("cls")
        print("*********************************\n")
        print("GAME OVER, YOUR SCORE IS", self.score)
        print("\n*********************************")
        exit(0)

    def export_data(self):
        return {"score": self.score,
                "lives": self.lives,
                "x": self.x, "y": self.y,
                "tank": self.tank, "mxtank": self.mxtank}

    def import_data(self, data):
        self.x = data["x"] or 0
        self.x = data["y"] or 0
        self.tank = data["tank"] or 0
        self.mxtank = data["mxtank"] or 1
        self.lives = data["lives"] or 3
        self.score = data["score"] or 0
