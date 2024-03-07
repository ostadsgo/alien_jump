import pgzrun

WIDTH = 800
HEIGHT = 600

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 50, 0)

# Actors
background = Actor("background")
alien = Actor("alien")
alien.pos = (50, 550)

cactus = Actor("cactus")
cactus.pos = (WIDTH - 50, HEIGHT - 50)
# variables
velocity_y = 0
gravity = 1
score = 0
game_over = False


def draw():
    if game_over:
        screen.draw.text("Game Over", (WIDTH // 2, HEIGHT // 2), color=red, fontsize=60)
    else:
        background.draw()
        alien.draw()
        cactus.draw()
        screen.draw.text(str(score), (WIDTH // 2, 50 ), color=white)


def update():
    global velocity_y
    global score
    global game_over
    cactus.x -= 5


    if keyboard.up:
        velocity_y = -20
        score += 1
    if keyboard.right:
        alien.x += 5
    if keyboard.left:
        alien.x -= 5

    alien.y += velocity_y
    velocity_y += gravity

    if alien.colliderect(cactus):
        game_over = True

    if alien.y > HEIGHT - 50:
        velocity_y = 0
        alien.y = HEIGHT - 50


pgzrun.go()
