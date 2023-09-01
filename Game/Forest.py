from Base import Base
from random import randint as rand



class Forest():
    
    def __init__(self):
        self.image_forest = Base.inst.image_forest
        self.image_fire = Base.inst.image_fire
        self.image_stump = Base.inst.image_stump
        self.bonus = 100
        
        Base.inst.gen_obj(self.image_forest)
        


    def fire_forest(self, Y, X, image_fire = "🔥"):
            Base.inst.map_game[Y][X] = image_fire
            
            

    
    def rand_fire(self):
         self.Yf, self.Xf  = Base.inst.rand_place((Base.inst.height - 1), (Base.inst.width - 1), 0)
         coord = self.print_fire(self.Yf, self.Xf)
         return coord
         
         
         
  
    def print_fire(self, Y, X):
        if Base.inst.map_game[Y][X] == self.image_forest:
            Base.inst.map_game[Y][X] = self.image_fire
            
            return Y, X
        else:
            return 0 


    def spreading_fire(self, Y, X, fire):
        
        if X >= 0:
            if Base.inst.map_game[Y][X - 1] == self.image_forest:
                X -= 1
                self.print_fire(Y, X)
                fire.append((Y, X))

        if X < Base.inst.width-1:
            if Base.inst.map_game[Y][X + 1] == self.image_forest:
                X += 1
                self.print_fire(Y, X) 
                fire.append((Y, X))     
                   
        if Y >= 0:
            if Base.inst.map_game[Y - 1][X] == self.image_forest:
                Y -= 1
                self.print_fire(Y, X)
                fire.append((Y, X))     
                
        if Y < Base.inst.height-1:
            if Base.inst.map_game[Y + 1][X] == self.image_forest:
                Y += 1
                self.print_fire(Y, X)
                fire.append((Y, X))
                
                
            
             
    
    def negative_fire(self, fire, RIP_forest):
        Y, X = fire[rand(0,len(fire) - 1)]
        RIP_forest.append([Y, X])
        Base.inst.map_game[Y][X] = self.image_stump
        self.spreading_fire(Y, X, fire)
        fire.remove((Y,X))

    def regeneration_map(self, RIP_forest):
        if len(RIP_forest) > 0:
            Y, X = RIP_forest[0]
            RIP_forest.pop(0)
            Base.inst.map_game[Y][X] = Base.inst.free_place
            


   

    
