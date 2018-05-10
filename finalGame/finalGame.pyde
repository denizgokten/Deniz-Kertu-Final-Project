add_library('sound')
import random 
import copy
# import os


# global path
# path= os.getcwd() 
# print path


class Creature:
    def __init__(self,x,y,r,vx,F):
        self.x=x #xpos
        self.y=y #ypos
        self.r=r #radius
        self.w=self.r*2 #diameterx
        self.h=self.r*2 #diametery
        self.vx=vx #velocityx
        self.vy=0 #velocityy
        self.F=4 #nr of frames
        self.f=0 
    
    def update(self):
        self.x+=self.vx
        self.y+=self.vy
 
    def display(self):
        self.update()
        if self.vx != 0 or self.vy !=0:
            self.f = (self.f+0.1)%self.F
        # stroke(0,255,40)
        # noFill()
        # ellipse(self.x-game.x,self.y,self.w,self.h)
        # stroke(255,50,0)
        
class Player(Creature):
    def __init__(self,x,y,r,vx,F,img,vy):
        Creature.__init__(self,x,y,r,vx,F)
        self.keyHandler={LEFT:False,RIGHT:False,UP:False,DOWN:False}
        self.vy=vy 
        self.img=loadImage(img)
        # self.scoreSound=SoundFile(this, '/Users/denizgokten/Desktop/Final Project/Deniz-Kertu-Final-Project/finalGame/finalGame/Aww.mp3')
        # self.crashSound=SoundFile(this, '/Users/denizgokten/Desktop/Final Project/Deniz-Kertu-Final-Project/finalGame/finalGame/crash.mp3')
        
    
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
                game.lives -= 1
                # self.crashSound.play()
                game.player.x=500
                game.player.y=800
                if game.lives == 0:
                    game.state='gameover'
                    # game.gameoverSound.play()
        for c in game.chicks: 
            if self.distance(c) < self.r+c.r:
                game.removeChick()
                game.increaseCarSpeed()
                game.score += 10
                # self.scoreSound.play()
        

    def moving(self):
         
        if self.keyHandler[DOWN]:
            self.vy=2
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

        if self.keyHandler[UP]:
            image(self.keyImage[UP],self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f)*self.w,0,int(self.f+1)*self.w,self.h)
        elif self.keyHandler[LEFT]:
            image(self.keyImage[LEFT],self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f+1)*self.w,0,int(self.f)*self.w,self.h)
        elif self.keyHandler[RIGHT]:
            image(self.keyImage[RIGHT],self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f)*self.w,0,int(self.f+1)*self.w,self.h)    
        else:
            image(self.keyImage[DOWN],self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f+1)*self.w,0,int(self.f)*self.w,self.h)

        
            
    def update(self):
        self.collosion()
        self.checkBorders()
        self.moving()
            
    
class Car(Creature):
    def __init__(self,x,y,r,vx,F,img): 
        Creature.__init__(self,x,y,r,vx,F)
        imglist=[loadImage('finalGame/car2.png'), loadImage('finalGame/car.png')]
        self.img=imglist[img]

        
    def update(self):
        Creature.update(self)
        if self.x < (0-self.r) or self.x > (game.w+self.r):
            print("car should remove")
            game.removeCar(self)
            
    def display(self):
        self.update()
        if self.vx != 0 or self.vy !=0:
            self.f = (self.f+0.1)%self.F
        # stroke(0,255,40)
        # noFill()
        # ellipse(self.x-game.x,self.y,self.w,self.h)
        # stroke(255,50,0)
        image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h)
    
            
class babyChick(Creature):
    def __init__(self,x,y,r,vx,F,img): 
        Creature.__init__(self,x,y,r,vx,F) 
        self.img=loadImage(img)
        
    def display(self):
        image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h)
    
class Life(Creature):
    def __init__(self, x, y, r, vx, F, img):
        Creature.__init__(self, x, y, r, vx, F)
        self.img = loadImage(img)
        
    def display(self):
        image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h)
    
xPoints = [0, 1024]
yPoints = [192, 317, 479, 612]

# global myCars
# myCars = [] 

class Game:
    def __init__(self):
        self.w=1024
        self.h=800
        self.player=Player(500,800,45,0,4,'front.png',0)
        self.paused= False
        self.state='menu'
        self.name= ''
        self.score=0
        self.lives=3
        self.startTime = millis()
        self.myCars=[]

    def createGame(self):
        self.x=0
        self.y=0
        self.chickcnt=0
        self.bgIMG=loadImage('finalGame/Road.png')
        self.chicks=[]
        self.cars=[]
        self.player.keyImage={LEFT:loadImage('finalGame/side.png'),RIGHT:loadImage('finalGame/side.png'),UP:loadImage('finalGame/back.png'),DOWN:loadImage('finalGame/front.png')}
        
        # self.gameoverSound=SoundFile(this,  '/Users/denizgokten/Desktop/Final Project/Deniz-Kertu-Final-Project/finalGame/finalGame/gameover.mp3')
        # self.pauseSound=SoundFile(this, '/Deniz-Kertu-Final-Project/finalGame/finalGame/pause.mp3')
        # print self.pauseSound
        # self.pauseSound=SoundFile(this, path + "/finalgame/pause.mp3")

        
        self.myCars.append(Car(xPoints[1], yPoints[0], 60,-1,1,0))
        self.myCars.append(Car(xPoints[0], yPoints[1], 60,1,1,1))
        self.myCars.append(Car(xPoints[1], yPoints[2], 60,-1,1,0))
        self.myCars.append(Car(xPoints[0], yPoints[3], 60,1,1,1))
        

        #Creating worms/baby chicks
        self.chicks.append(babyChick(500,55,40,1,0,'finalGame/lion.png'))
        
        # self.bgMusic=SoundFile(this, '/Users/denizgokten/Desktop/Final Project/Deniz-Kertu-Final-Project/finalGame/finalGame/RUN.mp3')
        # self.bgMusic.loop()
    def display(self):
        image(self.bgIMG,0,0) #put the background yay
        
        for car in self.cars:
            car.update()
            car.display()

            
        self.player.update()
        self.player.display()
        
        self.chicks[0].display()
        #create a global chickcounter, which is initially zero, which will update after a chick is eaten
                        
        #for future score counting
        fill(231,21,107)
        textSize(50)
        text("SCORE: " + str(self.score),10,40)
        text("LIVES: "+ str(self.lives),10,100) 
    
    def update(self):
        # Updating cars list
        now = millis()
        if now - self.startTime > 1200:
            self.startTime = now
            randCar = random.randint(0, 3)
            self.cars.append(copy.copy(self.myCars[randCar]))
        print ("cars", len(self.cars) )
            

    def removeCar(self, car):
        if car in self.cars:
            self.cars.remove(car)
        print 'del'
        
    def removeChick(self):
        del self.chicks[0]
        self.chicks.append(babyChick(random.randint(100, 924),random.randint(30, 770),40,1,0,'finalGame/lion.png'))
    
    def increaseCarSpeed(self): 
         
        for car in self.cars:
            if car.vx<0:
                car.vx-=0.05
            else:
                car.vx += 0.05
        
        for car in self.myCars:
            if car.vx<0:
                car.vx-=0.05
            else:
                car.vx += 0.05

game = Game()

def setup():
    size(game.w,game.h)
    background(0)
    game.createGame()


    
def draw():
    # myFont = createFont
    global textSize    
    if game.state=="menu":
        background(loadImage('finalGame/menu.png'))
        text("SHEEP ON THE RUN",110,160)
        noFill()
        noStroke()
        rect(570, 320, 150, 100)
        text("GO",570,400)
        textSize(85)
        fill(245)

    elif game.state == 'play': 
        if not game.paused:
            game.display()
            game.update()
        else:
            fill(123,191,20)
            textSize(100)
            text('STOPPP',350,400)
    elif game.state == 'gameover':
        # game.gameoverSound.play()
        background(loadImage('finalGame/gameover.png'))
        noFill()
        noStroke()
        rect(330, 510, 350, 120)
        fill(234,148,185)
        textSize(65)
        text("YOUR SCORE: " + str(game.score) ,270,230)
        text("GO AGAIN",330,570)
    elif game.state == 'replay':
        for i in game.cars: 
            game.removeCar(i)
        game.state='play'
        game.score=0
        game.lives=3
        game.display()
        game.chicks.insert(0, babyChick(500,55,40,1,0,'finalGame/lion.png'))
        game.myCars=[]
        game.myCars.append(Car(xPoints[1], yPoints[0], 60,-1,0,0))
        game.myCars.append(Car(xPoints[0], yPoints[1], 60,1,1,1))
        game.myCars.append(Car(xPoints[1], yPoints[2], 60,-1,0,0))
        game.myCars.append(Car(xPoints[0], yPoints[3], 60,1,1,1))
        game.update()


    
def keyPressed():
    game.player.keyHandler[keyCode]=True
    if game.state=='play':
        print (keyCode)
        game.player.keyHandler[keyCode]=True
        if keyCode == 80:
            game.paused = not game.paused
            # game.pauseSound.play()
            
         
def keyReleased():
    game.player.keyHandler[keyCode]=False
    
def mouseClicked():
    if game.state=='menu' and 570 <= mouseX <= 720 and 320 <= mouseY <= 420:
        game.state='play'
        # game.bgMusic.loop()

    elif game.state=='gameover' and 330 <= mouseX <= 680 and 510 <= mouseY <= 630:
        game.state='replay'
        # game.bgMusic.loop()

        
