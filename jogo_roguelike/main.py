import random
import math
from pygame import Rect

WIDTH = 640
HEIGHT = 480
TITLE = "Dungeon Roguelike"

TILE_SIZE = 32
ROWS = HEIGHT // TILE_SIZE
COLS = WIDTH // TILE_SIZE

# Representação da masmorra
# W = parede (Wall), . = chão (Floor)
dungeon_map = [
    "WWWWWWWWWWWWWWWW",
    "W..............W",
    "W.WWW.WWWW.WWW.W",
    "W.W..........W.W",
    "W.W.WW.WWWW.WW.W",
    "W...W....W....W.",
    "WWWWWWWWWWWWWWWW"
]

# Herói
hero = Actor("hero_idle", (TILE_SIZE * 2, TILE_SIZE * 2))
hero.speed = 2

# Inimigo
enemy = Actor("enemy_idle", (TILE_SIZE * 10, TILE_SIZE * 3))
enemy.speed = 1
enemy.direction = random.choice(["up", "down", "left", "right"])

# Sons (adicione seus próprios arquivos em sounds/)
music.set_volume(0.3)
sounds_enabled = True
try:
    music.play("music")
except:
    print("Adicione um arquivo sounds/music.wav para a música.")

def is_wall(x, y):
    col = int(x // TILE_SIZE)
    row = int(y // TILE_SIZE)
    if 0 <= row < len(dungeon_map) and 0 <= col < len(dungeon_map[0]):
        return dungeon_map[row][col] == "W"
    return True

def move_actor(actor, dx, dy):
    new_x = actor.x + dx
    new_y = actor.y + dy
    if not is_wall(new_x, new_y):
        actor.x = new_x
        actor.y = new_y
        if sounds_enabled:
            try:
                sounds.step.play()
            except:
                pass

def update():
    # Movimento do herói
    if keyboard.left:
        move_actor(hero, -hero.speed, 0)
    if keyboard.right:
        move_actor(hero, hero.speed, 0)
    if keyboard.up:
        move_actor(hero, 0, -hero.speed)
    if keyboard.down:
        move_actor(hero, 0, hero.speed)

    # Movimento do inimigo aleatório
    dx, dy = 0, 0
    if enemy.direction == "left":
        dx = -enemy.speed
    elif enemy.direction == "right":
        dx = enemy.speed
    elif enemy.direction == "up":
        dy = -enemy.speed
    elif enemy.direction == "down":
        dy = enemy.speed

    if not is_wall(enemy.x + dx, enemy.y + dy):
        enemy.x += dx
        enemy.y += dy
    else:
        enemy.direction = random.choice(["up", "down", "left", "right"])

    # Colisão com inimigo
    if hero.colliderect(enemy):
        print("Você foi pego!")

def draw():
    screen.clear()
    for row in range(len(dungeon_map)):
        for col in range(len(dungeon_map[row])):
            tile = dungeon_map[row][col]
            color = (50, 50, 50) if tile == "W" else (180, 180, 180)
            screen.draw.filled_rect(Rect(col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE), color)

    hero.draw()
    enemy.draw()
