
class Game:
    def __init__(self):
        self.w=1024
        self.x=0
        self.y=0
        self.h=800
        self.g=700
        self.player=Player(500,700,30,900,0)
        self.score=0
        self.cnt=0
        self.platforms=[]
        self.cars=[]
        self.car=Car(0, 400, 40, 400,2)
        self.car1=Car(1024, 600, 40, 400,-2)
        
    #def createGame(self):
       
    def display(self):
        #fill(255)
        #stroke(255)
        #line(0,self.g,self.w,self.g)
        self.player.display()
        self.car.display()
        self.car1.display()
        #for future score counting
        text(str(self.score),10,25)
        
class Creature:
    def __init__(self,x,y,r,g,vx):
        self.x=x
        self.y=y
        self.g=g
        self.r=r
        self.w=self.r*2
        self.h=self.r*2
        self.vx=vx
        self.vy=0
        self.dir=1
        
    def update(self):

        self.x+=self.vx
        self.y+=self.vy
 
    def display(self):
        self.update()
        stroke(0,255,40)
        noFill()
        ellipse(self.x-game.x,self.y,self.r*2,self.r*2)
        stroke(255,50,0)
        line(self.x-self.r-game.x,self.g,self.x+self.r-game.x,self.g)
            
    
    
class Player(Creature):
    def __init__(self,x,y,r,g,vx):
        Creature.__init__(self,x,y,r,g,vx)
        self.keyHandler={LEFT:False,RIGHT:False,UP:False,DOWN:False}
        
    def update(self):
        print self.keyHandler
        if self.keyHandler[DOWN]:
            self.vy=2
            self.dir=1
        elif self.keyHandler[UP]:
            self.vy=-2
            self.dir=-1
        else:
            self.vy=0
        
        if self.keyHandler[LEFT]:
            self.vx=-2
            self.dir=-1
        elif self.keyHandler[RIGHT]:
            self.vx=2
            self.dir=1
        else: 
            self.vx=0
            
        self.x+=self.vx
        self.y+=self.vy
            
    
class Car(Creature):
    def __init__(self,x,y,r,g,vx): 
        Creature.__init__(self,x,y,r,g,vx)
        
    def update 
        
         
    
    

#class Food(Creature):
    



game = Game()

def setup():
    size(game.w,game.h)
    background(0)
    
    
def draw():
    background(0)
    game.display()
    
def keyPressed():
    print (keyCode)
    game.player.keyHandler[keyCode]=True
         
def keyReleased():
    game.player.keyHandler[keyCode]=False
        
