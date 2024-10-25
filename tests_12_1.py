# Задача "Проверка на выносливость"
import unittest

class Runner:                   # Объекты класса для тестирования
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):      # ТЕСТЫ
    def test_walk(self):
        obj_runner = Runner('Бегун')
        n = 10
        while n > 0:
            obj_runner.walk()
            n -= 1
        self.assertEqual(obj_runner.distance, 50)

    def test_run(self):
        obj_runner = Runner('Бегун_2')
        n = 10
        while n > 0:
            obj_runner.run()
            n -= 1
        self.assertEqual(obj_runner.distance, 100)

    def test_challenge(self):
        obj_runner1 = Runner('Бегун_3')
        obj_runner2 = Runner('Бегун_4')
        n = 10
        while n > 0:
            obj_runner1.walk()
            obj_runner2.run()
            n -= 1
        self.assertNotEqual(obj_runner1.distance, obj_runner2.distance)

if __name__ == '__main__':
    unittest.main()