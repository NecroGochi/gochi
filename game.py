import sys
import random
from board import *
from sprites.creatures.character import *
from sprites.creatures.boss import *
from sprites.items.shootingweapon import *
from Configure.enemies_config import *
from Menu.level_up_menu import LevelUpMenu
from Menu.defeated_menu import DefeatedMenu
from Menu.win_menu import WinMenu


# Initialize Pygame
pygame.init()

# Set the window size
window_width = 192 * 5
window_height = 108 * 5
window = pygame.display.set_mode((window_width, window_height))


pygame.display.set_caption("Camera Scrolling")

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set font
font = pygame.font.Font(None, 32)

# Set player properties
player_size = 50
player_speed = 20

board = Board(window_width, window_height, 1715, 875, 255, 55)

clock = pygame.time.Clock()


def display_time(time, color):
    font_option = pygame.font.Font(None, 50)
    text = font_option.render(convert_time_to_str(time), True, color)
    text_rect = text.get_rect(center=(window_width // 2, 50))
    window.blit(text, text_rect)


def display_level(level, color):
    font_option = pygame.font.Font(None, 50)
    text = font_option.render("Level: " + str(level), True, color)
    text_rect = text.get_rect(center=(100, 50))
    window.blit(text, text_rect)


def display_exp_bar(player):
        pygame.draw.rect(window, (255, 255, 255), (40, 80, 400, 10))
        pygame.draw.rect(window, (0, 0, 155), (40, 80, player.actual_exp * 400 / player.max_exp, 10))


def convert_time_to_str(time):
    return str(math.floor(time / 60)) + ":" + str(math.floor(time % 60))


def generate_enemies(time, player, enemies, boss_appear):
    quantity_population = [0, 1, 2]
    positions_x = []
    positions_y = []
    for position in range(0, player.hitbox.x - 200):
        positions_x.append(position)
    for position in range(player.hitbox.x + 200, 1920):
        positions_x.append(position)
    for position in range(0, player.hitbox.y - 200):
        positions_y.append(position)
    for position in range(player.hitbox.y + 200, 1080):
        positions_y.append(position)
    if time / 60 < 1:
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Spinach["Size"], Spinach["Color"], Spinach["Speed"],
                        Spinach["AP"], Spinach["DP"], Spinach["HP"], Spinach["Exp"], Spinach["Image"])
            enemies.append(foe)
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Dog["Size"], Dog["Color"], Dog["Speed"],
                        Dog["AP"], Dog["DP"], Dog["HP"], Dog["Exp"], Dog["Image"])
            enemies.append(foe)
    if 1 < time / 60 < 2:
        if boss_appear[0]:
            boss_appear[0] = False
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Boss(enemy_position_x, enemy_position_y, Giga_Spinach["Size"], Giga_Spinach["Color"],
                       Giga_Spinach["Speed"], Giga_Spinach["AP"], Giga_Spinach["DP"], Giga_Spinach["HP"],
                       Giga_Spinach["Exp"], Giga_Spinach["Image"])
            enemies.append(foe)
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Dog["Size"], Dog["Color"], Dog["Speed"],
                        Dog["AP"], Dog["DP"], Dog["HP"], Dog["Exp"], Dog["Image"])
            enemies.append(foe)
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Cockroach["Size"], Cockroach["Color"], Cockroach["Speed"],
                        Cockroach["AP"], Cockroach["DP"], Cockroach["HP"], Cockroach["Exp"], Cockroach["Image"])
            enemies.append(foe)
    if 2 < time / 60 < 3:
        if boss_appear[1]:
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Boss(enemy_position_x, enemy_position_y, Giga_Dog["Size"], Giga_Dog["Color"],
                       Giga_Dog["Speed"], Giga_Dog["AP"], Giga_Dog["DP"], Giga_Dog["HP"],
                       Giga_Dog["Exp"], Giga_Dog["Image"])
            enemies.append(foe)
            boss_appear[1] = False
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Cockroach["Size"], Cockroach["Color"], Cockroach["Speed"],
                        Cockroach["AP"], Cockroach["DP"], Cockroach["HP"], Cockroach["Exp"], Cockroach["Image"])
            enemies.append(foe)
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Super_Spinach["Size"], Super_Spinach["Color"],
                        Super_Spinach["Speed"], Super_Spinach["AP"], Super_Spinach["DP"], Super_Spinach["HP"],
                        Super_Spinach["Exp"], Super_Spinach["Image"])
            enemies.append(foe)
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Angry_Dog["Size"], Angry_Dog["Color"], Angry_Dog["Speed"],
                        Angry_Dog["AP"], Angry_Dog["DP"], Angry_Dog["HP"], Angry_Dog["Exp"], Angry_Dog["Image"])
            enemies.append(foe)
    if 3 < time / 60 < 4:
        if boss_appear[2]:
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Boss(enemy_position_x, enemy_position_y, Giga_Cockroach["Size"], Giga_Cockroach["Color"],
                       Giga_Cockroach["Speed"], Giga_Cockroach["AP"], Giga_Cockroach["DP"], Giga_Cockroach["HP"],
                       Giga_Cockroach["Exp"], Giga_Cockroach["Image"])
            enemies.append(foe)
            boss_appear[2] = False
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Super_Spinach["Size"], Super_Spinach["Color"],
                        Super_Spinach["Speed"], Super_Spinach["AP"], Super_Spinach["DP"], Super_Spinach["HP"],
                        Super_Spinach["Exp"], Super_Spinach["Image"])
            enemies.append(foe)
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Bookworm["Size"], Bookworm["Color"], Bookworm["Speed"],
                        Bookworm["AP"], Bookworm["DP"], Bookworm["HP"], Bookworm["Exp"], Bookworm["Image"])
            enemies.append(foe)
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Super_Bookworm["Size"], Super_Bookworm["Color"],
                        Super_Bookworm["Speed"], Super_Bookworm["AP"], Super_Bookworm["DP"], Super_Bookworm["HP"],
                        Super_Bookworm["Exp"], Super_Bookworm["Image"])
            enemies.append(foe)
    if 4 < time / 60 < 5:
        if boss_appear[3]:
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Boss(enemy_position_x, enemy_position_y, Giga_Bookworm["Size"], Giga_Bookworm["Color"],
                       Giga_Bookworm["Speed"], Giga_Bookworm["AP"], Giga_Bookworm["DP"], Giga_Bookworm["HP"],
                       Giga_Bookworm["Exp"], Giga_Bookworm["Image"])
            enemies.append(foe)
            boss_appear[3] = False
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Super_Spinach["Size"], Super_Spinach["Color"],
                        Super_Spinach["Speed"], Super_Spinach["AP"], Super_Spinach["DP"], Super_Spinach["HP"],
                        Super_Spinach["Exp"], Super_Spinach["Image"])
            enemies.append(foe)
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Bookworm["Size"], Bookworm["Color"], Bookworm["Speed"],
                        Bookworm["AP"], Bookworm["DP"], Bookworm["HP"], Bookworm["Exp"], Bookworm["Image"])
            enemies.append(foe)
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Super_Bookworm["Size"], Super_Bookworm["Color"],
                        Super_Bookworm["Speed"], Super_Bookworm["AP"], Super_Bookworm["DP"], Super_Bookworm["HP"],
                        Super_Bookworm["Exp"], Super_Bookworm["Image"])
            enemies.append(foe)
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Ghost["Size"], Ghost["Color"], Ghost["Speed"],
                        Ghost["AP"], Ghost["DP"], Ghost["HP"], Ghost["Exp"], Ghost["Image"])
            enemies.append(foe)
    if 5 < time / 60:
        if boss_appear[4]:
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Boss(enemy_position_x, enemy_position_y, Giga_Book["Size"], Giga_Book["Color"],
                       Giga_Book["Speed"], Giga_Book["AP"], Giga_Book["DP"], Giga_Book["HP"],
                       Giga_Book["Exp"], Giga_Book["Image"])
            foe.is_final_boss()
            enemies.append(foe)
            boss_appear[4] = False
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Boss(enemy_position_x, enemy_position_y, Giga_Spinach["Size"], Giga_Spinach["Color"],
                       Giga_Spinach["Speed"], Giga_Spinach["AP"], Giga_Spinach["DP"], Giga_Spinach["HP"],
                       Giga_Spinach["Exp"], Giga_Spinach["Image"])
            enemies.append(foe)
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Boss(enemy_position_x, enemy_position_y, Giga_Dog["Size"], Giga_Dog["Color"],
                       Giga_Dog["Speed"], Giga_Dog["AP"], Giga_Dog["DP"], Giga_Dog["HP"],
                       Giga_Dog["Exp"], Giga_Dog["Image"])
            enemies.append(foe)
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Boss(enemy_position_x, enemy_position_y, Giga_Cockroach["Size"], Giga_Cockroach["Color"],
                       Giga_Cockroach["Speed"], Giga_Cockroach["AP"], Giga_Cockroach["DP"], Giga_Cockroach["HP"],
                       Giga_Cockroach["Exp"], Giga_Cockroach["Image"])
            enemies.append(foe)
        quantity = random.choice(quantity_population)
        for one in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, Super_Bookworm["Size"], Super_Bookworm["Color"],
                        Super_Bookworm["Speed"], Super_Bookworm["AP"], Super_Bookworm["DP"], Super_Bookworm["HP"],
                        Super_Bookworm["Exp"], Super_Bookworm["Image"])
            enemies.append(foe)
    return boss_appear


# Set Fonts
font_title = pygame.font.Font(None, 64)
font_options = pygame.font.Font(None, 32)


def game():
    # Set initial player position
    player = Character(board.width, board.height)
    enemies = []
    boss_appear = [True, True, True, True, True]
    new_weapons = [ShootingWeapon(0, 0), AreaWeapon(0, 0)]
    start_time = pygame.time.get_ticks()
    not_defeated_final_boss = True
    show_stat_up = 0

    defeated_menu = DefeatedMenu(window, window_width, window_height, font_title, font_options)
    win_menu = WinMenu(window, window_width, window_height, font_title, font_options)
    level_up_menu = LevelUpMenu(window, window_width, window_height, font_title, font_options)
    level_up_menu.weapon_level_up.add_item_to_menu_option(player.items[0].name)
    for weapon in new_weapons:
        level_up_menu.new_weapon_menu.add_item_to_menu_option(weapon.name)

    # Game loop
    running = True
    while running and player.actual_hp > 0 and not_defeated_final_boss:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                    for item in player.items:
                        item.left = 1
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                    for item in player.items:
                        item.left = 0
                elif event.key == pygame.K_UP:
                    player.go_up()
                elif event.key == pygame.K_DOWN:
                    player.go_down()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.velocity_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.velocity_y = 0
        # Calculate game time
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
        elapsed_seconds = round(elapsed_time / 1000, 0)

        player.collide_board(board.border_x1, board.border_x2, board.border_y1, board.border_y2)
        player.update_position()
        for item in player.items:
            item.move(player.hitbox.x, player.hitbox.y)
        for enemy in enemies:
            if board.border_y1 == player.hitbox.y or board.border_y2 == player.hitbox.y:
                player.velocity_y = 0
            if board.border_x1 == player.hitbox.x or board.border_x2 == player.hitbox.x:
                player.velocity_x = 0
            enemy.move(player.hitbox.x, player.hitbox.y, player.velocity_x, player.velocity_y)
        for enemy in enemies:
            for weapon in player.items:
                if weapon.type == "Rect":
                    enemy.collide_weapon(weapon.hitbox[0], player.items[0].power + player.ap)
                if weapon.type == "Circle":
                    enemy.collide_weapon_circle(weapon.hitbox[0], player.items[0].power + player.ap)
            player.collide_enemy(enemy.hitbox, elapsed_seconds, enemy.hit, enemy.ap)
            # remove enemy and get exp
            if enemy.actual_hp <= 0:
                if enemy.boss:
                    if enemy.final_boss:
                        not_defeated_final_boss = False
                enemies.remove(enemy)
                player.get_exp(enemy.exp)
                # Get level
                if player.actual_exp > player.max_exp:
                    for level_up in range(player.actual_exp // player.max_exp):
                        option_number = level_up_menu.run_loop()
                        if option_number[0] == 0:
                            player.grow_stat()
                            show_stat_up = 100
                        if option_number[0] == 1:
                            player.items[option_number[1]].get_level()
                            show_stat_up = 100
                        if option_number[0] == 2:
                            player.items.append(new_weapons[option_number[1]])
                            level_up_menu.new_weapon_menu.delete_item(new_weapons[option_number[1]].name)
                            level_up_menu.weapon_level_up.add_item_to_menu_option(new_weapons[option_number[1]].name)
                            new_weapons.remove(new_weapons[option_number[1]])
                    player.get_level()

        if elapsed_seconds % 5 == 0:
            generate = True
        else:
            generate = False

        if generate:
            boss_appear = generate_enemies(elapsed_seconds, player, enemies, boss_appear)

        # Update the camera position based on the player's position
        board.update_camera_position(player.hitbox.x, player.hitbox.y)
        # Update the background position based on the player's position
        board.update_background_position()
        # Clear the screen
        window.fill(black)
        window.blit(board.background, (board.background_x, board.background_y))

        # Render game objects based on the camera position
        for item in player.items:
            item.render(window, (50, 50, 155), board.camera_x, board.camera_y)
        player.render(window, white, board.camera_x, board.camera_y)
        for enemy in enemies:
            enemy.render(window, board.camera_x, board.camera_y)

        if show_stat_up != 0:
            show_stat_up -= 1
            player.render_text("Stat up", (0, 0, 0), window, board.camera_x, board.camera_y)

        # player information
        display_time(elapsed_seconds, (0, 0, 0))
        display_level(player.level, (0, 0, 0))
        display_exp_bar(player)
        # Update the display
        pygame.display.flip()

    if not_defeated_final_boss:
        defeated_menu.run_loop()
    else:
        win_menu.run_loop()
