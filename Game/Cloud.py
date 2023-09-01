from Base import Base
from random import randint as rand
from time import monotonic




class Cloud():

    def __init__(self):
        self.image_c = Base.inst.image_cloud
        self.image_l = Base.inst.image_lightning
        self.Y, self.X = Base.inst.rand_place((Base.inst.height - 1), (Base.inst.width - 1), 0)
        self.tmp_cloud = Base.inst.map_game[self.Y][self.X]
        
    
      
    def get_coordinates(self):
        return self.Y, self.X

        
    def move_cloud(self):
        
        i = rand(1 , 2)
        if i == 1:
            Base.inst.map_game[self.Y][self.X] = self.image_c
            
        elif i == 2:
            Base.inst.map_game[self.Y][self.X] = self.image_l
            return self.tmp_cloud
            
        
    
    def back(self):
            Base.inst.map_game[self.Y][self.X] = self.tmp_cloud


    def save_game(self):
        data = {
            "tmp": self.tmp_cloud
        }      
        return data
    

    def download_game(self, data):
         self.tmp_cloud = data["tmp"]
     
   

         

