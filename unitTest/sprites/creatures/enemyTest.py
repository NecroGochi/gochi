import unittest
from sprites.creatures.enemy import Enemy


class MyTestCase(unittest.TestCase):
    def test_collide_weapon_circle_attack_higher_then_defence(self):
        enemy = Enemy(50, 50, 20, 5, 5, 5, 100, 5, "../../../Images/Monsters/szpinak_monster.png")
        enemy.collide_weapon_circle([50, 50, 100], 10)
        self.assertEqual(enemy.actual_health_points, 95)

    def test_collide_weapon_circle_attack_lower_then_defence(self):
        enemy = Enemy(50, 50, 20, 5, 5, 5, 100, 5, "../../../Images/Monsters/szpinak_monster.png")
        enemy.collide_weapon_circle([50, 50, 100], 3)
        self.assertEqual(enemy.actual_health_points, 99)

    def test_collide_weapon_circle_negative_attack(self):
        enemy = Enemy(50, 50, 20, 5, 5, 5, 100, 5, "../../../Images/Monsters/szpinak_monster.png")
        enemy.collide_weapon_circle([50, 50, 100], -3)
        self.assertEqual(enemy.actual_health_points, 99)

    def test_collide_weapon_circle_negative_defence(self):
        enemy = Enemy(50, 50, 20, 5, 5, -5, 100, 5, "../../../Images/Monsters/szpinak_monster.png")
        enemy.collide_weapon_circle([50, 50, 100], 10)
        self.assertEqual(enemy.actual_health_points, 85)

    def test_collide_weapon_circle_attack_equal_defence(self):
        enemy = Enemy(50, 50, 20, 5, 5, 5, 100, 5, "../../../Images/Monsters/szpinak_monster.png")
        enemy.collide_weapon_circle([50, 50, 100], 5)
        self.assertEqual(enemy.actual_health_points, 99)

    def test_collide_weapon_circle_enemy_is_center_and_smaller(self):
        center = {
            'x': 50,
            'y': 50
        }
        enemy = Enemy(center['x'], center['y'], 20, 5, 5, 5, 100, 5, "../../../Images/Monsters/szpinak_monster.png")
        enemy.collide_weapon_circle([center['x'], center['y'], 100], 5)
        self.assertEqual(enemy.actual_health_points, 99)

    def test_collide_weapon_circle_enemy_is_center_and_the_same_size(self):
        center = {
            'x': 50,
            'y': 50
        }
        enemy = Enemy(center['x'], center['y'], 100, 5, 5, 5, 100, 5, "../../../Images/Monsters/szpinak_monster.png")
        enemy.collide_weapon_circle([center['x'], center['y'], 100], 5)
        self.assertEqual(enemy.actual_health_points, 99)

    def test_collide_weapon_circle_enemy_is_center_and_bigger(self):
        center = {
            'x': 50,
            'y': 50
        }
        enemy = Enemy(center['x'], center['y'], 200, 5, 5, 5, 100, 5, "../../../Images/Monsters/szpinak_monster.png")
        enemy.collide_weapon_circle([center['x'], center['y'], 100], 5)
        self.assertEqual(enemy.actual_health_points, 99)

    def test_collide_weapon_circle_enemy_is_outside(self):
        enemy = Enemy(0, 0, 20, 5, 5, 5, 100, 5, "../../../Images/Monsters/szpinak_monster.png")
        enemy.collide_weapon_circle([50, 50, 10], 5)
        self.assertEqual(enemy.actual_health_points, 100)

    def test_collide_weapon_circle_enemy_is_verge(self):
        enemy = Enemy(20, 30, 20, 5, 5, 5, 100, 5, "../../../Images/Monsters/szpinak_monster.png")
        enemy.collide_weapon_circle([50, 50, 10], 5)
        self.assertEqual(enemy.actual_health_points, 99)

    def test_collide_weapon_circle_enemy_is_partially_overlap(self):
        enemy = Enemy(25, 25, 20, 5, 5, 5, 100, 5, "../../../Images/Monsters/szpinak_monster.png")
        enemy.collide_weapon_circle([50, 50, 10], 5)
        self.assertEqual(enemy.actual_health_points, 99)

    def test_collide_weapon_circle_enemy_is_partially_overlap_only_side_x(self):
        enemy = Enemy(42, 40, 20, 5, 5, 5, 100, 5, "../../../Images/Monsters/szpinak_monster.png")
        enemy.collide_weapon_circle([50, 50, 10], 5)
        self.assertEqual(enemy.actual_health_points, 99)

    def test_collide_weapon_circle_enemy_is_partially_overlap_only_side_y(self):
        enemy = Enemy(40, 42, 20, 5, 5, 5, 100, 5, "../../../Images/Monsters/szpinak_monster.png")
        enemy.collide_weapon_circle([50, 50, 10], 5)
        self.assertEqual(enemy.actual_health_points, 99)



if __name__ == '__main__':
    unittest.main()
