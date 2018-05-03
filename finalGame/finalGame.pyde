import random 
import copy

class Creature:
    def __init__(self,x,y,r,vx):
        self.x=x
        self.y=y
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
        stroke(0,255,40)
        noFill()
        ellipse(self.x-game.x,self.y,self.r*2,self.r*2)
        stroke(255,50,0)
        
        

class Player(Creature):
    def __init__(self,x,y,r,vx):
        Creature.__init__(self,x,y,r,vx)
        self.keyHandler={LEFT:False,RIGHT:False,UP:False,DOWN:False}
    
    def distance(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5 
            
    def update(self):
        #print self.keyHandler
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
        
        #to detect collosion 
        # for c in self.cars: 
        #     if self.distance(c)<self.r+c.r: 
        #         pass
            
    
class Car(Creature):
    def __init__(self,x,y,r,vx): 
        Creature.__init__(self,x,y,r,vx)
        
    
        
    #Working on the way to delete cars that go out of frame
    def update(self):
        Creature.update(self)
        if self.x == (0-self.r) or self.x==(game.w+self.r):
            print 'ya'
            game.removeCar(self)
            


class babyChick(Creature):
    def __init__(self,x,y,r,vx): 
        Creature.__init__(self,x,y,r,vx) 
        self.vx=1
        
    def update(self):
        pass


xPoints = [0, 1024, 0, 1024, 0]
yPoints = [100, 200, 300, 400, 500]

global myCars
myCars = []
myCars.append(Car(xPoints[0], yPoints[0], 40,2)) 
myCars.append(Car(xPoints[1], yPoints[1], 40,-2))
myCars.append(Car(xPoints[2], yPoints[2], 40,2))
myCars.append(Car(xPoints[3], yPoints[3], 40,-2))
myCars.append(Car(xPoints[4], yPoints[4], 40,2))

class Game:
    def __init__(self):
        self.w=1024
        self.h=800
        self.g=700
        self.player=Player(500,700,30,0)
        self.paused= False
        self.state='MENU'
        self.name= ''
        self.score=0
        self.startTime = millis()

    def createGame(self):
        self.x=0
        self.y=0
        self.cnt=0
        self.chicks=[]
        self.cars=[]
    

        #Creating different cars 
        for i in range(5):
            self.cars.append(copy.deepcopy(myCars[i]))
        # self.cars.append(Car(self.xPoints[0], self.yPoints[0], 40,2)) 
        # self.cars.append(Car(self.xPoints[1], self.yPoints[1], 40,-2))
        # self.cars.append(Car(self.xPoints[2], self.yPoints[2], 40,2))
        # self.cars.append(Car(self.xPoints[3], self.yPoints[3], 40,-2))
        # self.cars.append(Car(self.xPoints[4], self.yPoints[4], 40,2))


        #Creating worms/baby chicks
        self.chicks.append(babyChick(150,300,10,1))
        self.chicks.append(babyChick(400,400,10,1))
        self.chicks.append(babyChick(700,300,10,1))
        self.chicks.append(babyChick(800,500,10,1))
        self.chicks.append(babyChick(350,200,10,1))
        self.chicks.append(babyChick(250,600,10,1))

    def display(self):
        #fill(255)
        #stroke(255)
        #line(0,self.g,self.w,self.g)
        self.player.update()
        self.player.display()
        for car in self.cars:
            car.update()
            car.display()
        # for c in self.chicks:
        #     c.display()
        self.chicks[0].display()
        #create a global chickcounter, which is initially zero, which will update after a chick is eaten
                
            
        #for future score counting
        text(str(self.score),10,25)
    
    def update(self):
        # Updating cars list
        now = millis()
        print now
        if now - self.startTime > 1000:
            self.startTime = now
            for i in range(5):
                self.cars.append(myCars[i])
    
    def removeCar(self, car):
        print("remove")
        self.cars.remove(car)
        # self.cars.append(Car(self.xPoints[0], self.yPoints[0], 40 ,2))
        
    
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
    print (keyCode)
    game.player.keyHandler[keyCode]=True
         
def keyReleased():
    game.player.keyHandler[keyCode]=False
        
