import time 
import os
import json
from pynput import keyboard
from time import monotonic
from Base import Base
from Hospital import Hospital
from Shop import Shop
from River import River
from Forest import Forest
from Cloud import Cloud
from Helicopter import Helicopter
from random import randint as rand



class Main():


    def __init__(self):
        Base()
       
        self.fire = monotonic()
        self.time_forest = monotonic()
        self.time_cloud = monotonic()
        self.time_cloud_delete = monotonic()
        self.fire_gen_forest = monotonic()
        self.regeneration = monotonic()
        self.timer_delete_cloud = 2
        self.TICK = 0
        self.clouds = []
        self.fire_forest = []
        self.RIP_forests = []



    def run_game(self):
        Base.inst.height , Base.inst.width = self.input()

        River()
        River()
        River()
        shop = Shop()
        hos = Hospital()
        helic = Helicopter()
        forest = Forest()

        Y_helic, X_helic = helic.begin_coord()
        helic.print_helic(Y_helic, X_helic)
        

        for _ in range(Base.inst.height * 2):
            Forest()
         
           
        def on_release(key):
            try:
                _str = key.char.lower()
                if _str == 'a':
                    helic.left_helic()
                if _str == 'w':
                    helic.up_helic()
                if _str == 'd':
                    helic.right_helic()
                if _str == 's':
                    helic.down_helic()
                if _str =='f':
                    helic.action(self.fire_forest)
                if _str == 'z':

                    data = {"Helicopter": helic.save_game(),
                            "Cloud": Cloud().save_game(),
                            "Base": Base.inst.save_game(),
                            "Main": self.save_game()}

                    with open("save game.json", "w") as sg:
                        json.dump(data, sg)
                if _str == 'x':
                    with open("save game.json", "r") as sg:
                        data = json.load(sg)
                        helic.download_game(data["Helicopter"])
                        Cloud().download_game(data["Cloud"])
                        Base.inst.download_game(data["Base"])
                        self.download_game(data["Main"])
            except :
                print("")
           
                
    
        listener = keyboard.Listener(
            on_press=None,
            on_release=on_release)
        listener.start()

             

        while True:

            if Base.inst.GAME_OVER == True:
                GO = "GAME OVER"
                os.system('cls')
                print(GO.center(len(GO)+10, '*'), "\n", "\n"," 🏆 " , helic.bonus )
                break
            
            print("")
            os.system('cls')
            print(" Магазин ", shop.image, "\n", "Госпиталь ", hos.image , "\n", "Действие - f" , '\n', "Сохраниние/загрузка - z/x ",  "\n", "Управление -w,a,s,d")
            print()
            print("🧡 " , helic.health,'/', helic.health_max, " 🧯 " , helic.tank,"/", helic.tank_max, " 🏆 ", helic.bonus, sep="")
            
            
               
            if (monotonic() - self.time_cloud) > 2:
                cloud = Cloud()
                tmp_cloud = cloud.move_cloud()
                cloud_Y, cloud_X = cloud.get_coordinates()
                if  tmp_cloud != Base.inst.image_forest:
                    self.clouds.append(cloud)
                else:
                    forest.fire_forest(cloud_Y, cloud_X)
                    self.fire_forest.append((cloud_Y, cloud_X))
                self.time_cloud = monotonic()
            
       

            if len(self.clouds) > 15:
                self.timer_delete_cloud = 1
            else:
                self.timer_delete_cloud = 3



            if (monotonic() - self.time_cloud_delete) > self.timer_delete_cloud:
                if len(self.clouds) > 0:
                    cloud = self.clouds[rand(0,len(self.clouds) - 1)]
                    ci_Y, cl_X = cloud.get_coordinates()
                    hil_Y, hil_X = helic.begin_coord()
                    if ci_Y == hil_Y and cl_X == hil_X:
                        helic.back(cloud.tmp_cloud)
                    else:
                        cloud.back()
                    self.clouds.pop(self.clouds.index(cloud))
                    self.time_cloud_delete = monotonic()
                
            helic.loss()

            if (monotonic() - self.time_forest) > 2.5:
                Forest()
                self.time_forest = monotonic()
            
            if (monotonic() - self.fire) > 3:
                
                f_coord = forest.rand_fire()
                if f_coord != 0:
                    self.fire_forest.append(f_coord)
                self.fire = monotonic()


            if len(self.fire_forest) > 5:
                if (monotonic() - self.fire_gen_forest) > 4:
                    forest.negative_fire(self.fire_forest,self. RIP_forests)
                    self.fire_gen_forest = monotonic()
                    if helic.bonus > 0:
                        helic.bonus -= forest.bonus
                if (monotonic() - self.regeneration) > 5.5:
                    forest.regeneration_map(self.RIP_forests)
                    self.regeneration = monotonic()

                    
            for i in range(Base.inst.height):
                print()
                for j in range(Base.inst.width):
                    print(Base.inst.map_game[i][j], end='')

         
            print("")
            print("Tick =", self.TICK, end="")
            print("")
            
            self.TICK += 1
            time.sleep(Base.inst.tick)


    def save_game(self):

        data ={
            "TICK": self.TICK,
            "fire_forest": self.fire_forest,
            "RIP_forests": self.RIP_forests,
        }
        return data
    

    def download_game(self, data):

        self.TICK = data["TICK"]
        self.fire_forest = data["fire_forest"]
        self.RIP_forests = data["RIP_forests"]


    def input(self):
        print("Укажите размеры поля: ")
        height = int(input("Высота: "))
        width = int(input("Ширина: "))
        return height, width



main = Main()
main.run_game()






