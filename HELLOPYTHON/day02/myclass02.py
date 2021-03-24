class Dog:
    def __init__(self):
        self.power_bark = 0 
    def taechFromHuman(self):
        self.power_bark += 1
        
class Bird(Dog):     
    def __init__(self):
        Dog.__init__(self)
        self.power_fly = 0;
    def exercise(self,power):
        self.power_fly+=power
        
if __name__ == '__main__':
    bir = Bird()
    print(bir.power_bark) 
    print(bir.power_fly) 
    bir.taechFromHuman()
    bir.exercise(5)
    print(bir.power_bark) 
    print(bir.power_fly) 
           
        
