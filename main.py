import asyncio,pgzero,pgzrun,pygame
from random import randint, choice
from string import ascii_letters

def draw():
    screen.clear()
    screen.blit("background",(0,0))
    if gameMode == 0:
        screen.blit("welcome",(120,80))
        screen.draw.text(f"Tu nombre: {user}", color="white", topleft=(200, 280))
        playAgain.draw()
    if gameMode == 1:
        valo.draw()
        monster.draw()
        screen.draw.text(f"Puntos: {score}", color="white", topleft=(10, 10))
    elif gameMode == 2:
        screen.blit("gameover",(160,120))
        screen.draw.text(f"{score} puntos", color="white", center=(320, 280),fontsize=50)
        playAgain.draw()

def update():
    global monster
    global score
    global speed
    global jumpDuration
    global monsterStartPoint
    global gameMode
   
    if gameMode == 0:
        # Welcome screen
        placePlayAgain()
    elif gameMode == 1:
        # Game dynamics
        # Monster moves
        monster.x = monster.x - speed
        if valo.colliderect(monster):
            # Check for loss condition
            gameMode = 2
            saveScore()
        elif monster.x < 0:
            # Send in a new monster
            monster = selectMonster()
            placeMonster()
            score = score + 100
            setDifficulty()
    elif gameMode == 2:
        # Game over screen
        placePlayAgain()

def on_mouse_down(pos):
    if gameMode == 0:
        # Start the game
        if playAgain.collidepoint(pos):
            resetGame()
    if gameMode == 1:
        if(valo.y == 350):
            animate(valo, pos=(60,150), tween="decelerate", duration=jumpDuration, on_finished=returnPosition)
    elif gameMode == 2:
        # Restart the game
        if playAgain.collidepoint(pos):
            resetGame()

def returnPosition():
    animate(valo, pos=(60,350),tween="accelerate", duration=jumpDuration)

def on_key_down(key):
    # User inputing their name
    # TODO: not compatible with mobile browsers
    global user
    global gameMode
    if gameMode == 0:
        if key == 8:
            user = user[0:-1]
        elif key == 13:
            gameMode = 1
        elif (key >= 65 and key <= 90) or (key >= 97 and key <= 122):
            pressedKey = chr(key)
            user += pressedKey
    
def selectMonster():   
    global lastMonster

    monsters = ["chica", "bunny", "foxy", "freddy2", "freddy"]
    
    if lastMonster in monsters: monsters.remove(lastMonster)

    lastMonster = monsterSelected = choice(monsters)

    return Actor(monsterSelected)

    

def placeValo():
    valo.x = 60
    valo.y = 350

def placeMonster():
    monster.x = 700
    monster.y = 350

def placePlayAgain():
    playAgain.x = 320
    playAgain.y = 380

def saveScore():
    pass

def setDifficulty():
    global speed
    global jumpDuration
    # Set difficulty
    if score == 1000:
        speed = 7
        jumpDuration = jumpDuration - 0.1
    elif score == 2000:
        speed = 9
        jumpDuration = jumpDuration - 0.1
    elif score == 3000:
        speed = 11
        jumpDuration = jumpDuration - 0.1
    elif score == 4000:
        speed = 13
    elif score == 5000:
        speed = 14
    elif score == 6000:
        speed = 15

def resetGame():
    global gameMode
    global score
    global speed
    global jumpDuration
    gameMode = 1
    score = 0
    speed = 5
    jumpDuration = 0.7
    placeMonster()

async def main():
    placeValo()
    placeMonster()
    pgzrun.go()
    await asyncio.sleep(0)

#
# Constants
#

WIDTH = 640
HEIGHT = 480
monsterStartPoint = 700
background = pygame.image.load("images/background.jpg")

#
# Variables
#

user = ""
score = 0
speed = 5
jumpDuration = 0.7
gameMode = 0
valo = Actor("valo")
lastMonster = ""
monster = selectMonster()
playAgain = Actor("play")
#
# Game start
#

asyncio.run(main())