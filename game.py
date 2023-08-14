import math
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


def generate_enemies(time, player, enemies, boss_appeared):
    quantity_population = [0, 1, 2]
    positions_x = []
    positions_y = []
    last_turn = 5

    for position in range(0, player.hitbox.x - 200):
        positions_x.append(position)
    for position in range(player.hitbox.x + 200, 1920):
        positions_x.append(position)
    for position in range(0, player.hitbox.y - 200):
        positions_y.append(position)
    for position in range(player.hitbox.y + 200, 1080):
        positions_y.append(position)

    monsters = [[Spinach, Dog],
                [Dog, Cockroach],
                [Cockroach, Super_Spinach, Angry_Dog],
                [Super_Spinach, Bookworm, Super_Bookworm],
                [Super_Spinach, Bookworm, Super_Bookworm, Ghost],
                [Giga_Spinach, Giga_Dog, Giga_Cockroach, Super_Bookworm]]

    boss_monsters = [None, Giga_Spinach, Giga_Dog, Giga_Cockroach, Giga_Bookworm, Giga_Book]

    turn = math.floor(time/60)

    if turn >= last_turn:
        enemies.extend(respawn_in_game(monsters[last_turn], boss_monsters[last_turn], positions_x, positions_y,
                                       quantity_population, boss_appeared[last_turn], True))
    else:
        enemies.extend(respawn_in_game(monsters[turn], boss_monsters[turn], positions_x, positions_y,
                                       quantity_population, boss_appeared[turn], False))

    boss_appeared[turn] = False

    return boss_appeared


def respawn_in_game(monsters, boss_monster, positions_x, positions_y, quantity_population, boss_appeared, is_last_wave):
    enemies = []
    enemies.extend(respawn_boss(boss_monster, positions_x, positions_y, boss_appeared, is_last_wave))
    enemies.extend(respawn_in_turn(monsters, positions_x, positions_y, quantity_population))
    return enemies


def respawn_in_turn(monsters, positions_x, positions_y, quantity_population):
    enemies = []
    for monster in monsters:
        quantity = random.choice(quantity_population)
        enemies.extend(respawn(monster, positions_x, positions_y, quantity))
    return enemies


def respawn_boss(monster, positions_x, positions_y, appeared, is_last_wave):
    boss = []
    if appeared:
        enemy_position_x = random.choice(positions_x)
        enemy_position_y = random.choice(positions_y)
        boss = [Boss(enemy_position_x, enemy_position_y, monster["Size"], monster["Color"],
                    monster["Speed"], monster["AP"], monster["DP"], monster["HP"], monster["Exp"], monster["Image"])]
        boss = is_last_boss(boss[0], is_last_wave)
    return boss


def is_last_boss(boss, is_last_wave):
    if is_last_wave:
        boss.is_final_boss()
    return [boss]


def respawn(monster, positions_x, positions_y, quantity):
    monsters = []
    for i in range(quantity):
        enemy_position_x = random.choice(positions_x)
        enemy_position_y = random.choice(positions_y)
        foe = Enemy(enemy_position_x, enemy_position_y, monster["Size"], monster["Color"],
                    monster["Speed"], monster["AP"], monster["DP"], monster["HP"], monster["Exp"], monster["Image"])
        monsters.append(foe)
    return monsters


# Set Fonts
font_title = pygame.font.Font(None, 64)
font_options = pygame.font.Font(None, 32)


def game():
    # Set initial player position
    player = Character(board.width, board.height)
    enemies = []
    boss_appear = [False, True, True, True, True, True]
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

def is_not_killed_final_boss(enemy):
    if enemy.final_boss:
        return False
    else:
        return True


def level_up(player, level_up_menu, new_weapons, show_stat_up):
    for level_up in range(player.actual_exp // player.max_exp):
        option_number = level_up_menu.run_loop()
        show_stat_up = choose_bonus(player, option_number, show_stat_up, new_weapons, level_up_menu)
    player.get_level()
    return show_stat_up


def choose_bonus(player, option_number, show_stat_up, new_weapons, level_up_menu):
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
    return show_stat_up


