from random import randint as rand


class Base():

    inst = None
    def __new__(cls):
        if Base.inst is None:
            Base.inst = super().__new__(cls)
        return Base.inst
    
    
        
    def __init__(self):
        self.image_forest = "🌴"
        self.image_fire = "🔥"
        self.image_stump = "⬛️"
        self.image_cloud = "💭"
        self.image_lightning = "⚡️"
        self.image_helicopter = "🚁"
        self.image_river = "🌊"
        self.free_place = "🟩"
        self.image_hospital = "🏪"
        self.image_shop = "🏩"

        self.bonus = 100

        self.height = 100
        self.width = 100
        self.map_game = self.gen_map()

        self.tick = 0.05

        self.GAME_OVER = False




    def gen_map(self):
        maps = []
        for i in range(self.height):
            maps.append([])
            for _ in range(self.width):
                maps[i].append(self.free_place)
        return maps
    

    def rand_place(self, H, W, begin):
        X = rand(begin, W)
        Y = rand(begin, H)
        return Y, X
        

    def gen_obj(self, image):
        Y, X = self.rand_place((self.height - 1), (self.width - 1), 0)

        if image == "🌊":
            Yr, Xr = self.rand_place((self.height // 2), (self.width // 2), 5)
            for _ in range(self.height * 2):
                self.map_game[Yr][Xr] = image 
                i = rand(1, 4)
                if i == 1 & Xr > 0:
                    Xr -= 1
                elif i == 2 & Xr < self.width - 2:
                    Xr += 1         
                elif i == 3 & Yr >= 0:
                    Yr -= 1
                elif i == 4 & Yr < self.height - 2:
                    Yr += 1 
                else:
                    continue 
        elif self.map_game[Y][X] == self.free_place: 
            self.map_game[Y][X] = image 
        else:
            self.gen_obj(image)
        


    def save_game(self):

        data = {
            "map_game": self.map_game
        }
        return data
    

    def download_game(self, data):
        self.map_game = data["map_game"] or self.gen_map()


