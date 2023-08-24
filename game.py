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


class Game:
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue_purple = (50, 50, 155)
    blue = (0, 0, 155)
    experience_bar_dimensions = (40, 80, 400, 10)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 32)
    font_title = pygame.font.Font(None, 64)
    font_options = pygame.font.Font(None, 32)
    is_respawn_bosses = [False, True, True, True, True, True]
    not_defeated_final_boss = True

    def __init__(self, window, window_width, window_height):
        # Set the window size
        self.window_width = window_width
        self.window_height = window_height
        self.window = window
        pygame.display.set_caption("Gochi Game")
        self.board = Board(self.window_width, self.window_height, 1715, 875, 255, 55)

        self.bosses = [None, Giga_Spinach, Giga_Dog, Giga_Cockroach, Giga_Bookworm, Giga_Book]
        self.monsters = [[Spinach, Dog],
                         [Dog, Cockroach],
                         [Cockroach, Super_Spinach, Angry_Dog],
                         [Super_Spinach, Bookworm, Super_Bookworm],
                         [Super_Spinach, Bookworm, Super_Bookworm, Ghost],
                         [Giga_Spinach, Giga_Dog, Giga_Cockroach, Super_Bookworm]]
        self.number_of_waves = len(self.monsters) - 1

    def play(self):
        # Set initial player position
        player = Character(self.board.width, self.board.height)
        enemies = []
        new_weapons = [ShootingWeapon(0, 0), AreaWeapon(0, 0)]
        start_time = pygame.time.get_ticks()
        show_stat_up = 0

        defeated_menu = DefeatedMenu(self.window, self.window_width, self.window_height, self.font_title,
                                     self.font_options)
        win_menu = WinMenu(self.window, self.window_width, self.window_height, self.font_title, self.font_options)
        level_up_menu = LevelUpMenu(self.window, self.window_width, self.window_height, self.font_title,
                                    self.font_options)
        level_up_menu.weapon_level_up.add_item_to_menu_option(player.items[0].name)
        for weapon in new_weapons:
            level_up_menu.new_weapon_menu.add_item_to_menu_option(weapon.name)

        # Game loop
        running = True
        while running and player.actual_health_points > 0 and self.not_defeated_final_boss:
            self.game_loop(player, start_time, enemies, show_stat_up, level_up_menu, new_weapons)

        if self.not_defeated_final_boss:
            defeated_menu.run_loop()
        else:
            win_menu.run_loop()

    def game_loop(self, player, start_time, enemies, show_stat_up, level_up_menu, new_weapons):
        for event in pygame.event.get():
            self.happened(event, player)
        # Calculate game time
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
        elapsed_seconds = round(elapsed_time / 1000, 0)

        player.collide_board(self.board.down_border, self.board.up_border, self.board.right_border,
                             self.board.left_border)
        player.update_position()
        for item in player.items:
            item.move(player.hitbox.x, player.hitbox.y)
        for enemy in enemies:
            self.move_enemy(player, enemy)
        for enemy in enemies:
            show_stat_up = self.collide(enemy, enemies, player, level_up_menu, new_weapons, show_stat_up,
                                        elapsed_seconds)

        if elapsed_seconds % 5 == 0:
            generate = True
        else:
            generate = False

        if generate:
            self.generate_enemies(elapsed_seconds, player, enemies)

        # Update the camera position based on the player's position
        self.board.update_camera_position(player.hitbox.x, player.hitbox.y)
        # Update the background position based on the player's position
        self.board.update_background_position()
        # Clear the screen
        self.window.fill(self.black)
        self.window.blit(self.board.background, (self.board.background_x, self.board.background_y))

        # Render game objects based on the camera position
        for item in player.items:
            item.render(self.window, self.board.camera_x, self.board.camera_y)
        player.render(self.window, self.board.camera_x, self.board.camera_y)
        for enemy in enemies:
            enemy.render(self.window, self.board.camera_x, self.board.camera_y)

        if show_stat_up != 0:
            show_stat_up -= 1
            player.render_text("Stat up", self.black, self.window, self.board.camera_x, self.board.camera_y)

        # player information
        self.display_time(elapsed_seconds)
        self.display_level(player.level)
        self.display_exp_bar(player)
        # Update the display
        pygame.display.flip()

    def happened(self, event, player):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self.push_key(event, player)
        elif event.type == pygame.KEYUP:
            self.pull_key(event, player)

    def push_key(self, event, player):
        if event.key == pygame.K_LEFT:
            player.go_left()
            self.update_items_status(player, 1)
        elif event.key == pygame.K_RIGHT:
            player.go_right()
            self.update_items_status(player, 0)
        elif event.key == pygame.K_UP:
            player.go_up()
        elif event.key == pygame.K_DOWN:
            player.go_down()

    @staticmethod
    def update_items_status(player, is_left):
        for item in player.items:
            item.left = is_left

    @staticmethod
    def pull_key(event, player):
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player.velocity_x = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            player.velocity_y = 0

    def move_enemy(self, player, enemy):
        if self.board.right_border == player.hitbox.y or self.board.left_border == player.hitbox.y:
            player.velocity_y = 0
        if self.board.down_border == player.hitbox.x or self.board.up_border == player.hitbox.x:
            player.velocity_x = 0
        enemy.move(player.hitbox.x, player.hitbox.y, player.velocity_x, player.velocity_y)

    def collide(self, enemy, enemies, player, level_up_menu, new_weapons, show_stat_up, elapsed_seconds):
        for weapon in player.items:
            self.collide_enemy_with_weapon(weapon, enemy, player)
        player.collide_enemy(enemy.hitbox, elapsed_seconds, enemy.hit, enemy.attack)
        # remove enemy and get exp
        if enemy.actual_health_points <= 0:
            show_stat_up = self.killed_enemy(enemy, enemies, player, level_up_menu, new_weapons, show_stat_up)
        return show_stat_up

    @staticmethod
    def collide_enemy_with_weapon(weapon, enemy, player):
        if weapon.type == "Rect":
            enemy.collide_weapon(weapon.hitbox[0], player.items[0].power + player.attack)
        if weapon.type == "Circle":
            enemy.collide_weapon_circle(weapon.hitbox[0], player.items[0].power + player.attack)

    def killed_enemy(self, enemy, enemies, player, level_up_menu, new_weapons, show_stat_up):
        if enemy.boss:
            self.not_defeated_final_boss = self.is_not_killed_final_boss(enemy)
        enemies.remove(enemy)
        player.get_experience_points(enemy.experience)
        # Get level
        if player.actual_experience_points > player.max_experience_points:
            show_stat_up = self.level_up(player, level_up_menu, new_weapons, show_stat_up)
        return show_stat_up

    @staticmethod
    def is_not_killed_final_boss(enemy):
        if enemy.final_boss:
            return False
        else:
            return True

    def level_up(self, player, level_up_menu, new_weapons, show_stat_up):
        for level_up in range(player.actual_experience_points // player.max_experience_points):
            option_number = level_up_menu.run_loop()
            show_stat_up = self.choose_bonus(player, option_number, show_stat_up, new_weapons, level_up_menu)
        player.get_level()
        return show_stat_up

    @staticmethod
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

    def generate_enemies(self, time, player, enemies):
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

        turn = math.floor(time/60)

        if turn >= self.number_of_waves:
            enemies.extend(self.respawn_boss(positions_x, positions_y, self.number_of_waves))
            enemies.extend(self.respawn_monsters(positions_x, positions_y, quantity_population, self.number_of_waves))
        else:
            enemies.extend(self.respawn_boss(positions_x, positions_y, turn))
            enemies.extend(self.respawn_monsters(positions_x, positions_y, quantity_population, turn))

    def respawn_monsters(self, positions_x, positions_y, quantity_population, turn):
        enemies = []
        for monster in self.monsters[turn]:
            quantity = random.choice(quantity_population)
            enemies.extend(self.respawn(monster, positions_x, positions_y, quantity))
        return enemies

    def respawn_boss(self, positions_x, positions_y, turn):
        boss = []
        type_boss = self.bosses[turn]
        if self.is_respawn_bosses[turn]:
            self.is_respawn_bosses[turn] = False
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            boss = [Boss(enemy_position_x, enemy_position_y, type_boss["Size"], type_boss["Color"],
                         type_boss["Speed"], type_boss["AP"], type_boss["DP"], type_boss["HP"],
                         type_boss["Exp"], type_boss["Image"])]
            boss = self.is_last_boss(boss[0], turn)
        return boss

    def is_last_boss(self, boss, turn):
        if turn == self.number_of_waves:
            boss.is_final_boss()
        return [boss]

    @staticmethod
    def respawn(monster, positions_x, positions_y, quantity):
        monsters = []
        for i in range(quantity):
            enemy_position_x = random.choice(positions_x)
            enemy_position_y = random.choice(positions_y)
            foe = Enemy(enemy_position_x, enemy_position_y, monster["Size"], monster["Color"],
                        monster["Speed"], monster["AP"], monster["DP"], monster["HP"], monster["Exp"], monster["Image"])
            monsters.append(foe)
        return monsters

    def display_time(self, time):
        font_option = pygame.font.Font(None, 50)
        text = font_option.render(self.convert_time_to_str(time), True, self.black)
        text_rect = text.get_rect(center=(self.window_width // 2, 50))
        self.window.blit(text, text_rect)

    def display_level(self, level):
        font_option = pygame.font.Font(None, 50)
        text = font_option.render("Level: " + str(level), True, self.black)
        text_rect = text.get_rect(center=(100, 50))
        self.window.blit(text, text_rect)

    def display_exp_bar(self, player):
        pygame.draw.rect(self.window, self.white, self.experience_bar_dimensions)
        pygame.draw.rect(self.window, self.blue, (self.experience_bar_dimensions[0],
                                                  self.experience_bar_dimensions[1],
                                                  player.actual_experience_points * 400 / player.max_experience_points,
                                                  self.experience_bar_dimensions[3]))

    @staticmethod
    def convert_time_to_str(time):
        return str(math.floor(time / 60)) + ":" + str(math.floor(time % 60))
