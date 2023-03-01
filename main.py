from random import randint
from constants import DIR_DICT, HELP


class Tank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'N'
        self.shots_fired = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
        self.target = self.generate_target()

    def __str__(self):
        return f'({self.x}, {self.y}) facing: {self.direction}\n' \
               f'{self.target} - target'

    def move(self, action_key):
        self.direction = DIR_DICT[action_key]

        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
        print(self)

    def generate_target(self):
        self.target = (self.x, self.y)
        while self.target == (self.x, self.y):
            self.target = (randint(-10, 10), randint(-10, 10))
        return self.target

    def fire(self):
        self.shots_fired[self.direction] += 1

        if self.target[0] == self.x and self.target[1] > self.y and self.direction == 'N':
            print('TARGET ELIMINATED')
            self.generate_target()
            return
        if self.target[0] == self.x and self.target[1] < self.y and self.direction == 'S':
            print('TARGET ELIMINATED')
            self.generate_target()
            return
        if self.target[1] == self.y and self.target[0] > self.x and self.direction == 'E':
            print('TARGET ELIMINATED')
            self.generate_target()
            return
        if self.target[1] == self.y and self.target[0] < self.x and self.direction == 'W':
            print('TARGET ELIMINATED')
            self.generate_target()
            return

        print('missed target')

    def info(self):
        print('** TANK INFO ** \n'
              f'direction:   {self.direction}\n'
              f'coordinates: {self.x, self.y}\n'
              f'* SHOOTING *\n'
              f'total:       {sum(self.shots_fired.values())}\n'
              f'north:       {self.shots_fired["N"]}\n'
              f'south:       {self.shots_fired["S"]}\n'
              f'east:        {self.shots_fired["E"]}\n'
              f'west:        {self.shots_fired["W"]}\n')


tank = Tank()
print(HELP)
print(f'Tank\'s starting position:\n{tank}')

while True:
    action = input().lower()

    if action in 'wasd' and len(action) == 1:
        tank.move(action)

    if action == ' ':
        tank.fire()
        print(tank)

    if action == 'i':
        tank.info()

    if action == 'q':
        print('GAME OVER')
        break
