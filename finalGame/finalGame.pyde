import random 
import copy

class Creature:
    def __init__(self,x,y,r,vx,img):
        self.x=x
        self.y=y
        self.r=r
        self.w=self.r*2
        self.h=self.r*2
        self.vx=vx
        self.vy=0
        self.f=0
        self.dir=1
        self.img=loadImage(img)
    
    def update(self):
        self.x+=self.vx
        self.y+=self.vy
 
    def display(self):
        self.update()
        stroke(0,255,40)
        noFill()
        ellipse(self.x-game.x,self.y,self.w,self.h)
        stroke(255,50,0)
        
       # if self.dir > 0:
       #     image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f)*self.w,0,int(self.f+1)*self.w,self.h)
       # else:
        #    image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f+1)*self.w,0,int(self.f)*self.w,self.h)
                 
        
        

class Player(Creature):
    def __init__(self,x,y,r,vx,img):
        Creature.__init__(self,x,y,r,vx,img)
        self.keyHandler={LEFT:False,RIGHT:False,UP:False,DOWN:False}
    
    def distance(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5 
    
    def checkBorders(self):
        if self.x-self.r < 0: 
            self.x=self.r 
        elif self.x+self.r > game.w: 
            self.x=game.w-self.r
        
        if self.y-self.r<0: 
            self.y=self.r
        elif self.y+self.r > game.h: 
            self.y=game.h-self.r
            
    def distance(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5 
    
    def collosion(self):
        for c in game.cars: 
            if self.distance(c) < self.r+c.r: 
                print "ups"
        for c in game.chicks: 
            if self.distance(c) < self.r+c.r: 
                print "njom" 
                
    def moving(self): 
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
        
                    
    def update(self):
        self.collosion()
        self.checkBorders()
        self.moving()
            
    
class Car(Creature):
    def __init__(self,x,y,r,vx,img): 
        Creature.__init__(self,x,y,r,vx,img)
        
    def update(self):
        Creature.update(self)
        if self.x == (0-self.r) or self.x==(game.w+self.r):
            game.removeCar(self)
            


class babyChick(Creature):
    def __init__(self,x,y,r,vx,img): 
        Creature.__init__(self,x,y,r,vx,img) 
        self.vx=1
        
    def update(self):
        pass


xPoints = [0, 1024]
yPoints = [192, 317, 479, 612]

global myCars
myCars = [] 
myCars.append(Car(xPoints[1], yPoints[0], 55,-1,'car1.png'))
myCars.append(Car(xPoints[0], yPoints[1], 55,1,'car1.png'))
myCars.append(Car(xPoints[1], yPoints[2], 55,-1,'car1.png'))
myCars.append(Car(xPoints[0], yPoints[3], 55,1,'car1.png'))

class Game:
    def __init__(self):
        self.w=1024
        self.h=800
        self.player=Player(500,700,45,0,'car1.png')
        self.paused= False
        self.state='MENU'
        self.name= ''
        self.score=0
        self.startTime = millis()

    def createGame(self):
        self.x=0
        self.y=0
        self.cnt=0
        self.bgIMG=loadImage('finalGame/Road.png')
        self.chicks=[]
        self.cars=[]


        #Creating worms/baby chicks
        self.chicks.append(babyChick(150,300,10,1,'car1.png'))
        
    def display(self):
        image(self.bgIMG,0,0) #put the background yay
        
        self.player.update()
        self.player.display()
        
        for car in self.cars:
            car.update()
            car.display()
        self.chicks[0].display()
        #create a global chickcounter, which is initially zero, which will update after a chick is eaten
                
            
        #for future score counting
        text(str(self.score),10,25)
    
    def update(self):
        # Updating cars list
        now = millis()
        if now - self.startTime > 945:
            self.startTime = now
            randCar = random.randint(0, 3)
            self.cars.append(copy.deepcopy(myCars[randCar]))
    
    def removeCar(self, car):
        self.cars.remove(car)
        
    
game = Game()

def setup():
    size(game.w,game.h)
    background(0)
    game.createGame()
    
    
def draw():
    background(0)
    game.display()
    game.update()
    
def keyPressed():
    game.player.keyHandler[keyCode]=True
         
def keyReleased():
    game.player.keyHandler[keyCode]=False
        
