import pygame
import time
import random

pygame.init()

height=600
width=800

gameDisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption('Racer Delight')

pause=False

Brown=(150,75,0)
green=(0,200,0)
White=(255,255,255)
Yellow=(255,255,0)
Blue=(0,0,255)
Black=(0,0,0)
Red=(200,0,0)
hover_green=(0,255,0)
grey=(125,125,125)
hover_Red=(255,0,0)
Cyan=(0,255,255)

clock=pygame.time.Clock()
carimg=pygame.image.load(r'C:\Users\NAMANJEET SINGH\Pictures\Saved Pictures\Car.png')
crash_Sound=pygame.mixer.Sound(r"C:\Users\NAMANJEET SINGH\Music\crash_metal_med2.wav")
pygame.mixer.music.load(r"C:\Users\NAMANJEET SINGH\Music\rock-out-complete_proud_music_preview.mp3")

#functions
def Score(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Score: "+str(count),True,Black)
    gameDisplay.blit(text,(0,0))

def button(msg,x,y,w,h,ic,ac,action=None):
    # Hovering button
    click=pygame.mouse.get_pressed()
    mouse=pygame.mouse.get_pos()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action!=None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    # text on button
    smalltext = pygame.font.Font('freesansbold.ttf', 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textsurf, textrect)


def car(x,y):
    gameDisplay.blit(carimg,(x,y))

def obstacles(ox,oy,ow,oh,color):
    pygame.draw.rect(gameDisplay,color,[ox,oy,ow,oh])

def text_objects(text,font):
    textsurface=font.render(text,True,Black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect=text_objects(text,largetext)
    TextRect.center=((width/2),(height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    GameLoop()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_Sound)
    crash =True
    while crash:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        largetext = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Crashed", largetext)
        TextRect.center = ((width / 2), (height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play Again",150,450,100,50,green,hover_green,GameLoop)
        button("Quit",550,450,100,50,Red,hover_Red,QuitGame)

        pygame.display.update()
        clock.tick(15)

def Intro():
    intro =True

    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(Cyan)
        largetext = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Racers Delight", largetext)
        TextRect.center = ((width / 2), (height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play",150,450,100,50,green,hover_green,GameLoop)
        button("Quit",550,450,100,50,Red,hover_Red,QuitGame)

        pygame.display.update()
        clock.tick(15)

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause=False

def QuitGame():
    pygame.quit()
    quit()

def Paused():

    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()


        largetext = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Paused", largetext)
        TextRect.center = ((width / 2), (height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue",150,450,100,50,green,hover_green,unpause)
        button("Quit",550,450,100,50,Red,hover_Red,QuitGame)

        pygame.display.update()
        clock.tick(15)

def GameLoop():
    global pause
    pygame.mixer.music.play(-1)
    x=(width*0.45)
    y=(height*0.8)

    #variables
    x_change=0
    o_startx=random.randrange(0,width)
    o_starty=-height
    o_width=100
    o_height=100
    o_speed=7
    score=0

    Exit=False
    while not Exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_p:
                    pause=True
                    Paused()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                    x_change=0


        #calling
        x+=x_change
        gameDisplay.fill(grey)

        obstacles(o_startx,o_starty,o_width,o_height,Brown)
        o_starty+=o_speed
        car(x,y)
        Score(score)

        #boundaries
        if x>width-82 or x<0:
            crash()

        #animation of obstacles
        if o_starty>height:
            o_starty=0-height
            o_startx=random.randrange(0,width)
            score+=1
            if score%5==0:
                o_speed+=2

        #crashing
        if y<o_starty+o_height:
            if x>o_startx and x<o_startx + o_width or x+82>o_startx and x+82<o_startx+o_width:
                crash()

        pygame.display.update()
        clock.tick(60)

Intro()
GameLoop()
pygame.quit()
quit()