import pygame
import random

#init
pygame.init() 
score = 0
clock = pygame.time.Clock()

#screen size
screenWidth = 480 
screenHeight = 640 
screen = pygame.display.set_mode((screenWidth,screenHeight))  

#background image
background = pygame.image.load("background.png")

#character
character = pygame.image.load("character.png")
characterSize = character.get_rect().size  
characterWidth = characterSize[0]
characterHeight = characterSize[1]
characterXpos = (screenWidth / 2) - (characterWidth / 2)
characterYpos = screenHeight - characterHeight

#X,Y location
toX = 0
toY = 0

#speed
characterSpeed = 0.6

#random number of shit
randomNumber = 30
poSpeed = 10

#enemy
enemy = pygame.image.load("enemy.png")
enemySize = enemy.get_rect().size
enemyWidth = enemySize[0]
enemyHeight = enemySize[1]
enemyXpos = 200
enemyYpos = 100

#Title
pygame.display.set_caption("분리수거 당번 피지컬 테스트")

#font 
game_font = pygame.font.Font(None,40) 

#play time
totalTime = 10
startTicks = pygame.time.get_ticks()

#Event
running = True
while running:  
    dt = clock.tick(20)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                toX -= characterSpeed
            if event.key == pygame.K_RIGHT:
                toX += characterSpeed
            if event.key == pygame.K_UP:
                toY -= characterSpeed
            if event.key == pygame.K_DOWN:
                toY += characterSpeed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                toX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                toY = 0 
    
    #character movement & hit frame
    characterXpos += toX * dt
    characterYpos += toY * dt
    
    
    #limit setting, Landscape
    if characterXpos < 0:
        characterXpos = 0
    elif characterXpos > screenWidth - characterWidth:
        characterXpos = screenWidth - characterWidth
    #limit setting, Portrait
    if characterYpos < 0:
        characterYpos = 0
    elif characterYpos > screenHeight - characterHeight:
        characterYpos = screenHeight - characterHeight
    
    
    randomNumber = random.randrange(1,200)
    randomNumber2 = random.randrange(1,440)
    
    if enemyYpos > 640:
        enemyYpos = randomNumber
        enemyXpos = randomNumber2
        score += 1
        poSpeed += 2
    
    enemyYpos += poSpeed
        
    #hit box
    characterRect = character.get_rect()
    characterRect.left = characterXpos
    characterRect.top = characterYpos
    
    enemyRect = enemy.get_rect()
    enemyRect.left = enemyXpos
    enemyRect.top = enemyYpos
    
    if characterRect.colliderect(enemyRect):
        print("YOU DIED")
        running = False

    elapsedTime = (pygame.time.get_ticks()) / 1000
    timer = game_font.render(str(int(totalTime - elapsedTime)), True, (255,255,255))
    scoree = game_font.render(str(score), True, (200,200,200))

    screen.blit(background, (0,0)) 
    screen.blit(character, (characterXpos , characterYpos))
    screen.blit(enemy, (enemyXpos , enemyYpos))
    screen.blit(timer, (10,10))
    screen.blit(scoree, (10,30))
    pygame.display.update() 

pygame.quit()   