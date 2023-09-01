from Base import Base
from Cloud import Cloud



class Helicopter():

    def __init__(self):
        self.image = Base.inst.image_helicopter
        self.tank = 0
        self.tank_max = 1
        self.health = 3
        self.health_max = 3
        self.bonus = 0
        self.Y, self.X = Base.inst.rand_place((Base.inst.height - 1), (Base.inst.width - 1), 0)
        self.tmp_helic = ''


    def print_helic(self, Y, X):
        if Base.inst.map_game[Y][X] != Base.inst.image_cloud and Base.inst.map_game[Y][X] != Base.inst.image_lightning:
            self.tmp_helic = Base.inst.map_game[Y][X]
            Base.inst.map_game[Y][X] = self.image


    def begin_coord(self):
        return self.Y, self.X
        

    def up_helic(self):
        if self.Y > 0:
            if Base.inst.map_game[self.Y][self.X] != Base.inst.image_cloud and Base.inst.map_game[self.Y][self.X] != Base.inst.image_lightning:
                Base.inst.map_game[self.Y][self.X] = self.tmp_helic
            self.Y -= 1
            self.print_helic(self.Y, self.X)


    def down_helic(self):
        if self.Y < Base.inst.height-1:
            if Base.inst.map_game[self.Y][self.X] != Base.inst.image_cloud and Base.inst.map_game[self.Y][self.X] != Base.inst.image_lightning:
                Base.inst.map_game[self.Y][self.X] = self.tmp_helic
            self.Y += 1
            self.print_helic(self.Y, self.X)
        

    def left_helic(self):
        if self.X > 0:
            if Base.inst.map_game[self.Y][self.X] != Base.inst.image_cloud and Base.inst.map_game[self.Y][self.X] != Base.inst.image_lightning:
                Base.inst.map_game[self.Y][self.X] = self.tmp_helic
            self.X -= 1
            self.print_helic(self.Y, self.X)
            

    def right_helic(self):
        if self.X < Base.inst.width-1:
            if Base.inst.map_game[self.Y][self.X] != Base.inst.image_cloud and Base.inst.map_game[self.Y][self.X] != Base.inst.image_lightning:
                Base.inst.map_game[self.Y][self.X] = self.tmp_helic
            self.X += 1
            self.print_helic(self.Y, self.X)

    def action(self, fire):
        if self.tmp_helic == Base.inst.image_river and self.tank < self.tank_max:
            self.tank += 1
        if self.tmp_helic == Base.inst.image_fire and self.tank > 0:
            self.tmp_helic = Base.inst.image_forest
            self.bonus += Base.inst.bonus
            self.tank -= 1
            fire.remove((self.Y, self.X))
        if self.tmp_helic == Base.inst.image_hospital and self.health < self.health_max and self.bonus >= 500:
            self.health += 1
            self.bonus -= 500
        if self.tmp_helic == Base.inst.image_shop and self.bonus >= 1000:
            self.tank_max += 1
            self.bonus -= 1000


    def loss(self):
        if self.health == 0:
            Base.inst.GAME_OVER = True
        if Base.inst.map_game[self.Y][self.X] == Base.inst.image_lightning:
            Base.inst.map_game[self.Y][self.X] = self.image
            self.tmp_helic = Cloud().tmp_cloud
            self.health -= 1
           

    def back(self, tmp):
        if Base.inst.map_game[self.Y][self.X] == Base.inst.image_cloud:
            Base.inst.map_game[self.Y][self.X] = self.image
            self.tmp_helic = tmp

           


    def save_game(self):
        
        data = {
            "bonus": self.bonus,
            "health": self.health,
            "tank": self.tank,
            "tmp_helic": self.tmp_helic,
            "max_tank": self.tank_max,
            "Y": self.Y,
            "X": self.X
        }

        return data
    
    def download_game(self, data):
        self.bonus = data["bonus"] or 0
        self.health = data["health"] or 3
        self.tank = data["tank"] or 0
        self.tmp_helic = data["tmp_helic"]
        self.tank_max = data["max_tank"] or 1
        self.Y = data["Y"]
        self.X = data["X"]


   