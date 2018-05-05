import random 
import copy
add_library('sound')

class Creature:
    def __init__(self,x,y,r,vx,img,F):
        self.x=x #xpos
        self.y=y #ypos
        self.r=r #radius
        self.w=self.r*2 #diameterx
        self.h=self.r*2 #diametery
        self.vx=vx #velocityx
        self.vy=0 #velocityy
        self.F=4 #nr of frames
        self.f=0 
        self.img=loadImage(img)
    
    def update(self):
        self.x+=self.vx
        self.y+=self.vy
 
    def display(self):
        self.update()
        if self.vx != 0 or self.vy !=0:
            self.f = (self.f+0.1)%self.F
        stroke(0,255,40)
        noFill()
        ellipse(self.x-game.x,self.y,self.w,self.h)
        stroke(255,50,0)
        
class Player(Creature):
    def __init__(self,x,y,r,vx,img,F,vy):
        Creature.__init__(self,x,y,r,vx,img,F)
        self.keyHandler={LEFT:False,RIGHT:False,UP:False,DOWN:False}
        self.vy=vy 
        self.animationCounter=0
        
    
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
                # game.chickcnt += 1
                game.removeChick()
                print game.chickcnt
                print "njom" 
                
    def moving(self):
         
        if self.keyHandler[DOWN]:
            self.vy=2
            #animationIndex=self.animationCounter % 4 
        elif self.keyHandler[UP]:
            self.vy=-2
        else:
            self.vy=0
        
        if self.keyHandler[LEFT]:
            self.vx=-2    
        elif self.keyHandler[RIGHT]:
            self.vx=2
        else: 
            self.vx=0
        
        self.x+=self.vx
        self.y+=self.vy
        self.animationCounter +=1
        
        # print(self.keyImage[UP])
        if self.keyHandler[UP]:
            image(self.keyImage[UP],self.x-self.r-game.x,self.y-self.r,self.w,self.h,0,int(self.f)*self.h,self.w,int(self.f+1)*self.h)
        elif self.keyHandler[LEFT]:
            print('here')
            image(self.keyImage[LEFT],self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f+1)*self.w,0,int(self.f)*self.w,self.h)

        elif self.keyHandler[RIGHT]:
            image(self.keyImage[RIGHT],self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f)*self.w,0,int(self.f+1)*self.w,self.h)
            
        else:
            image(self.keyImage[DOWN],self.x-self.r-game.x,self.y-self.r,self.w,self.h,0,int(self.f)*self.h,self.w,int(self.f+1)*self.h)

        
            
    def update(self):
        self.collosion()
        self.checkBorders()
        self.moving()
            
    
class Car(Creature):
    def __init__(self,x,y,r,vx,img,F): 
        Creature.__init__(self,x,y,r,vx,img,F)
        
    def update(self):
        Creature.update(self)
        if self.x == (0-self.r) or self.x==(game.w+self.r):
            game.removeCar(self)
            
            
class babyChick(Creature):
    def __init__(self,x,y,r,vx,img,F): 
        Creature.__init__(self,x,y,r,vx,img,F) 
        #self.vx=1
        
    def update(self):
        pass


xPoints = [0, 1024]
yPoints = [192, 317, 479, 612]

global myCars
myCars = [] 
myCars.append(Car(xPoints[1], yPoints[0], 55,-1,'car1.png',0))
myCars.append(Car(xPoints[0], yPoints[1], 55,1,'car1.png',0))
myCars.append(Car(xPoints[1], yPoints[2], 55,-1,'car1.png',0))
myCars.append(Car(xPoints[0], yPoints[3], 55,1,'car1.png',0))

class Game:
    def __init__(self):
        self.w=1024
        self.h=800
        self.player=Player(500,700,45,0,'car1.png',4,0)
        self.paused= False
        self.state='menu'
        self.name= ''
        self.score=0
        self.startTime = millis()

    def createGame(self):
        self.x=0
        self.y=0
        self.chickcnt=0
        self.bgIMG=loadImage('finalGame/Road.png')
        self.chicks=[]
        self.cars=[]
        self.player.keyImage={LEFT:loadImage('finalGame/side.png'),RIGHT:loadImage('finalGame/side.png'),UP:loadImage('finalGame/back.png'),DOWN:loadImage('finalGame/front.png')}
        

        #Creating worms/baby chicks
        self.chicks.append(babyChick(150,300,10,1,'car1.png',0))
        
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
        
    def removeChick(self):
        del self.chicks[0]
        self.chicks.append(babyChick(random.randint(100, 924),random.randint(30, 770),30,1,'car1.png',0))
        
    
game = Game()

def setup():
    size(game.w,game.h)
    background(0)
    game.createGame()
    
    
def draw():
    if game.state=="menu":
        background(255,78,90)
        if game.state=='menu' and game.w//2 <= mouseX <= game.w//2+160 and game.h//2-30 <= mouseY <= game.h//2+10:
            fill(250,255,50)
        else: 
            fill(255)
            textSize(50)
            text("Welcome to SHEEP ON THE GO",70,300)
            text("Play Game",game.w//2,game.h//2)
    elif game.state == 'play': 
        if not game.paused:
            background(0) 
            game.display()
            game.update()
        else:
            fill(250,55,50)
            textSize(80)
            text('STOPPP',350,400)
    # elif game.state=='inputName':
    #     background(0)
    #     textSize(40)
    #     text("Please enter your name",game.w//2,game.h//2-200)
    #     text(game.name,game.w//2,game.h//2)
    # background(0) 
    # game.display()
    # game.update()
    
def keyPressed():
    game.player.keyHandler[keyCode]=True
    if game.state=='play':
        print (keyCode)
        game.player.keyHandler[keyCode]=True
        
        if keyCode == 80:
            game.paused = not game.paused
            # game.pauseSound.play()
    elif game.state=='inputName':
       print keyCode, key, type(key)
       if keyCode == 8:
           game.name = game.name[:len(game.name)-1]
       elif keyCode == 10:
           f = open("highscores.csv","a")
           f.write(game.name+','+str(game.score)+'\n')
           f.close()
           game.__init__()
           game.createGame()
       elif type(key) != int :
           game.name += key
         
def keyReleased():
    game.player.keyHandler[keyCode]=False
    
def mouseClicked():
    if game.state=='menu' and game.w//2 <= mouseX <= game.w//2+160 and game.h//2-30 <= mouseY <= game.h//2+10:
       game.state='play'
        
