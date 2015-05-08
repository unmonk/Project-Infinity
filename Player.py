__author__ = 'Scott'
import pygame
import pytmx
from Constants import *
from Tools import *
from Projectile import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, lives):
        pygame.sprite.Sprite.__init__(self)
        ###############################################ANIMATION START############################################################
        #Stand Right
        self.idleRight = []
        for i in range(0, 5):
            self.idleRight.append(DATA['playerIdle'][i])
        #Stand Left
        self.idleLeft = []
        for i in range(0, 5):
            self.idleLeft.append(pygame.transform.flip(self.idleRight[i], True, False))
        #Walking Right Animation
        self.walkRight = []
        for i in range(0, 7):
            self.walkRight.append(DATA['playerRun'][i])
        #Walking Left Animation
        self.walkLeft = []
        for i in range(0, 7):
            self.walkLeft.append(pygame.transform.flip(self.walkRight[i], True, False))
        #Jump Right Animation
        self.jumpingRight = []
        self.jumpingRight.append(DATA['playerJump'][0])
        self.jumpingRight.append(DATA['playerJump'][1])
        #Jump Left Animation
        self.jumpingLeft = []
        self.jumpingLeft.append(pygame.transform.flip(self.jumpingRight[0], True, False))
        self.jumpingLeft.append(pygame.transform.flip(self.jumpingRight[1], True, False))
        #Player Slide/Wall Jump
        self.wallAnim = DATA['playerSlide'][0]
        #animation frames
        self.running = False
        self.runningFrame = 0
        self.frameTime = pygame.time.get_ticks()
        self.idleFrame = 0
        ####################################################END ANIMATION#############################################

        self.image = self.idleRight[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = "right"
        self.changeX = 0
        self.changeY = 0
        #What level char is on > move to game
        self.currentLevel = None
        #lives
        self.lives = lives
        #player State
        self.state = "none"
        #firing
        self.projectiles = []
        self.doublejump = 0
        self.powerupbool = False
        self.againstWall = False#tells the enemy class that player is against wall so ignore ChangeX

    def update(self, enemy):
        #print self.changeY
        self.death()
        self.rect.x += self.changeX
        self.handleCollision()
        self.mapMove()
        self.rect.y += self.changeY
        self.jumpingCollision()
        self.powerUp()
        self.updateAnimationFrames()
        if(self.againstWall == True):
            enemy.moveRelPlayer(0, self.changeY)
        else:    
            enemy.moveRelPlayer(self.changeX, self.changeY)
        #print(self.currentLevel)
        #self.exitCollision() #remove when the constant is fixed
        for k in self.projectiles:
            k.update()
            if k.active == False:
                self.projectiles.remove(k)






    def updateAnimationFrames(self):
        if pygame.time.get_ticks() - self.frameTime > 80:
            self.frameTime = pygame.time.get_ticks()
            if self.runningFrame == 6 or self.idleFrame == 4:
                self.runningFrame = 0
                self.idleFrame = 0
            else:
                self.runningFrame += 1
                self.idleFrame += 1



    def mapMove(self):
        movedmap = False
        if self.rect.right >= SCREEN_WIDTH - 500:
            difference = self.rect.right - (SCREEN_WIDTH-500)
            self.rect.right = SCREEN_WIDTH - 500
            self.currentLevel.shiftLevelX(-difference)
            movedmap = True
        elif self.rect.left <= 500:
            difference = 500 - self.rect.left
            self.rect.left = 500
            self.currentLevel.shiftLevelX(difference)
            movedmap = True
           

        if self.rect.bottom >= SCREEN_HEIGHT - 70:
            difference = self.rect.bottom - (SCREEN_HEIGHT-70)
            self.rect.bottom = SCREEN_HEIGHT - 70
            self.currentLevel.shiftLevelY(-difference)
            movedmap = True
            
        elif self.rect.top <= 150:
            difference = 150 - self.rect.top
            self.rect.top = 150
            self.currentLevel.shiftLevelY(difference)
            movedmap = True
            
            #supposed to move the enemy only if player triggers movement of level.

    def handleCollision(self):
        self.againstWall = False #reset flag each time this function is called
        tileCollision = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        for tile in tileCollision:
            if self.changeX > 0:
                self.rect.right = tile.rect.left                
            else:
                self.rect.left = tile.rect.right
            self.againstWall = True        
                
    def exitCollision(self):
        tileCollision = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_ENDOFLEVEL_LAYER].tiles, False)
        for tile in tileCollision:
            print("changed level")
            return 1
        return 0
    def powerUp(self):
        tileCollision = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_ITEM_LAYER].tiles, True)
        for tile in tileCollision:
            if self.powerupbool == False: #make sure player only gets one powerup     
                print("powerup")
                self.lives += 1
                heart.play()
                self.powerupbool = True
            return 1
        return 0
    def jumpingCollision(self):
        tileCollision = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        if len(tileCollision) > 0:
            for tile in tileCollision:
                if self.changeY > 0:
                    self.rect.bottom = tile.rect.top
                    self.changeY = 1

                    if self.direction == "right":
                        self.image = self.idleRight[self.idleFrame]
                        self.doublejump = 0
                    else:
                        self.image = self.idleLeft[self.idleFrame]
                        self.doublejump = 0
                else:
                    self.rect.top = tile.rect.bottom
                    self.changeY = 0
        else:
            self.changeY += 1
            if self.changeY > 0:
                if self.direction == "right":
                    self.image = self.jumpingRight[0]
                else:
                    self.image = self.jumpingLeft[0]

        if self.running and self.changeY == 1:
            if self.direction == "right":
                self.image = self.walkRight[self.runningFrame]
                self.doublejump = 0
            else:
                self.image = self.walkLeft[self.runningFrame]
                self.doublejump = 0


    #ground jump
    def jump(self):
        #self.rect.y += 20
        tileCollision = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        #self.rect.y -= 20
        #self.changeY = -25
        print(self.doublejump)
        if self.doublejump < 2:
            	if self.direction == "right":
                	self.image = self.jumpingRight[1]
            	else:
                	self.image = self.jumpingLeft[1]
        	self.changeY = -25
        	self.rect.y -= 20
        	if self.doublejump == 0:
            		jump1.play()
        	else:
            		jump2.play()
        	self.doublejump += 1
        else:
            return

    #death upon collision with death layer
    #add enemy collision
    def death(self):
        deathCollision = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_DEATH_LAYER].tiles, False)
        #enemyCollision = pygame.sprite.spritecollide(self, enemy, False)
        if len(deathCollision) > 0:
            self.rect.x = 0
            self.rect.y = 0
            self.lives -= 1
            print "DEBUG: LIVES:", self.lives


    def shoot(self):
        gun = self.rect.x, self.rect.y+75

        if (len(self.projectiles) < 1):
            if self.direction == "right":
                projectile = Projectile(gun, 50, "right")
            else:
                projectile = Projectile(gun, -50, "left")
            self.projectiles.append(projectile)
            print "DEBUG: shot fired"
            print self.projectiles


    def goRight(self):
        self.direction = "right"
        self.running = True
        self.changeX = 15

    def goLeft(self):
        self.direction = "left"
        self.running = True
        self.changeX = -15

    def stop(self):
        self.running = False
        self.changeX = 0
    def levelReset(self, x, y):
        self.rect.x = x
        self.rect.y = y
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for k in self.projectiles:
            k.display()
