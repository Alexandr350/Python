from Base import Base

class Shop():
    
    def __init__(self):
    
        self.image = Base.inst.image_shop
        Base.inst.gen_obj(self.image)