
class Game:
    def __init__(self):
        self.w=1024
        self.x=0
        self.h=800
        self.g=700
        self.player=Creature(500,700,30,900)
        
    #def createGame(self):
       
    def display(self):
        stroke(255)
        line(0,self.g,self.w,self.g)
        self.player.display()

        
        
    
    
class Creature:
    def __init__(self,x,y,r,g):
        self.x=x
        self.y=y
        self.g=g
        self.r=r
        self.w=self.r*2
        self.h=self.r*2
        self.vx=0
        self.vy=0
        
    def update(self):

        self.x+=self.vx
        self.y+=self.vy
 
    def display(self):
        self.update()
        stroke(255,255,50)
        noFill()
        ellipse(self.x-game.x,self.y,self.r*2,self.r*2)
        stroke(255,50,0)
        line(self.x-self.r-game.x,self.g,self.x+self.r-game.x,self.g)
            
    
    
#class Chicken(Creature):
    
#class Cars(Creature):
    



game = Game()

def setup():
    size(game.w,game.h)
    background(0)
    
    
def draw():
    background(0)
    game.display()
        
