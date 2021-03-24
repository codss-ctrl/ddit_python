class Dog:
    def __init__(self):
        self.power_bark = 0 
    def taechFromHuman(self):
        self.power_bark += 1
        
class Bird():     
    def __init__(self):
        self.power_fly = 0;
    def exercise(self,power):
        self.power_fly+=power
           
class GaeSae(Dog,Bird):     
    def __init__(self):
        Bird.__init__(self)
        Dog.__init__(self)


if __name__ == '__main__':
    gs = GaeSae()
    print(gs.power_bark)
    print(gs.power_fly)
    gs.exercise(5)
    gs.taechFromHuman()
    print(gs.power_bark)
    print(gs.power_fly)
          
        
