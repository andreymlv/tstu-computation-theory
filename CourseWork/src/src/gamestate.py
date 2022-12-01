from collections.abc import Callable
from dataclasses import dataclass
from random import randint

import pygame

from src.disk import Disk
from src.position import Position
from src.size import Size
from src.tower import Tower


def init() -> None:
    pygame.display.set_caption("Hanoi Tower")


def flat_map(f: Callable, xs) -> list:
    ys = []
    for x in xs:
        ys.extend(f(x))
    return ys


def random_color() -> pygame.Color:
    return pygame.Color((randint(0, 255), randint(0, 255), randint(0, 255)))


@dataclass()
class GameState:
    towers: list[Tower]
    over: bool

    def next(self):
        return self

    def poll(self):
        print("GameState", self.towers)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_m:
                        return MoveState(self.towers, False, 0)
                    case pygame.K_s:
                        return SolveState(self.towers, False)
                    case pygame.K_r:
                        return RestartState(self.towers, False)
                    case pygame.K_F1:
                        return HelpState(
                            self.towers,
                            False,
                            "s - Solve mode ; m - Move mode ; r - Restart game ;",
                        )
                    case pygame.K_q:
                        return GameState(self.towers, True)
        return self

    def render(self) -> None:
        screen_size = Size(800, 600)
        backgroud_color = pygame.Color((255, 255, 255))
        tower_color = pygame.Color((255, 0, 0))
        disk_color = pygame.Color((0, 255, 0))
        max_disks = len(self.fresh_towers()[0].disks)
        first_tower_x = screen_size.width / len(self.towers) / 4
        first_disk_x = screen_size.width / len(self.towers) / 8
        max_width_disk = 2 * first_disk_x + first_tower_x
        window = pygame.display.set_mode(screen_size)
        window.fill(backgroud_color)
        towers_rects: list[pygame.Rect] = []
        disks_rects: list[pygame.Rect] = []
        for i, tower in enumerate(self.towers):
            towers_rects.append(
                tower.draw(
                    Position(
                        first_tower_x + screen_size.width / len(self.towers) * i,
                        screen_size.height / 3,
                    ),
                    Size(first_tower_x * 2, screen_size.height),
                )
            )
            for j, disk in enumerate(tower.disks):
                position = Position(
                    first_disk_x + screen_size.width / max_disks * i,
                    100 * disk.weight,
                )
                disk_size = Size(max_width_disk / (j + 1), 100)
                print(disk, position, disk_size)
                disks_rects.append(disk.draw(position, disk_size))
        for tower in towers_rects:
            pygame.draw.rect(window, tower_color, tower)
        for disk in disks_rects:
            pygame.draw.rect(window, random_color(), disk)
        pygame.display.update()
        pygame.time.Clock().tick(1)

    def move(self, from_tower: int, to_tower: int):
        if self.can_move(from_tower, to_tower):
            towers: list[Tower] = self.towers.copy()
            temp_disk: Disk = towers[from_tower].last()
            towers[from_tower] = towers[from_tower].pop()
            towers[to_tower] = towers[to_tower].push(temp_disk)
            return GameState(towers, self.over)
        return self

    def hanoi_recursive(self) -> list:
        def strategy(
            disks: int, source: int, target: int, temp: int
        ) -> list[tuple[int, int]]:
            if disks == 0:
                return []
            return (
                strategy(disks - 1, source, temp, target)
                + [(source, target)]
                + strategy(disks - 1, temp, target, source)
            )

        steps: list[tuple[int, int]] = strategy(
            len(self.towers[0].disks), 0, len(self.towers) - 1, 1
        )
        history: list = [self]
        for step in steps:
            history.append(history[-1].step(step))
        return history

    def hanoi_iterative(self) -> list:
        def two_way_move(source, target, last_state):
            if last_state.can_move(source, target):
                return last_state.step((source, target))
            else:
                return last_state.step((target, source))

        disks: int = len(self.towers[0].disks)
        source: int = 0
        target: int = len(self.towers) - 1
        temp: int = 1
        history: list = [self]
        total: int = 2**disks - 1
        if disks % 2 == 0:
            for i in range(total):
                if i % 3 == 0:
                    history.append(two_way_move(source, temp, history[-1]))
                elif i % 3 == 1:
                    history.append(two_way_move(source, target, history[-1]))
                else:
                    history.append(two_way_move(temp, target, history[-1]))
        else:
            for i in range(total):
                if i % 3 == 0:
                    history.append(two_way_move(source, target, history[-1]))
                elif i % 3 == 1:
                    history.append(two_way_move(source, temp, history[-1]))
                else:
                    history.append(two_way_move(temp, target, history[-1]))
        return history

    def step(self, move: tuple[int, int]):
        return self.move(move[0], move[1])

    def can_move(self, from_tower: int, to_tower: int) -> bool:
        return self.towers[from_tower].can_pop() and self.towers[to_tower].can_push(
            self.towers[from_tower].last()
        )

    def fresh_towers(self) -> list[Tower]:
        disks: int = len(
            flat_map(
                lambda id: id,
                map(lambda tower: tower.disks, self.towers),
            )
        )
        towers: list[Tower] = list(map(lambda _: Tower([]), range(len(self.towers))))
        towers[0].disks = list(map(lambda x: Disk(x), range(disks, 0, -1)))
        return towers


@dataclass()
class RestartState(GameState):
    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE | pygame.K_SPACE | pygame.K_n:
                        return GameState(self.towers, False)
                    case pygame.K_y:
                        return GameState(self.fresh_towers(), False)
                    case pygame.K_F1:
                        return HelpState(
                            self.towers,
                            False,
                            "y - Yes, restart the game ; n - No, don't restart ;",
                        )
        return self


@dataclass()
class HelpState(GameState):
    help_text: str

    def poll(self):
        print("HelpState", self.help_text, self.towers)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE | pygame.K_SPACE:
                        return GameState(self.towers, False)
        return self


@dataclass()
class SelectState(GameState):
    selected_tower: int

    def poll(self):
        print("SelectState", self.selected_tower, self.towers)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE | pygame.K_SPACE:
                        return MoveState(self.towers, False, self.selected_tower)
                    case pygame.K_a | pygame.K_LEFT | pygame.K_h:
                        return SelectState(
                            self.towers,
                            False,
                            (self.selected_tower - 1) % len(self.towers),
                        )
                    case pygame.K_d | pygame.K_RIGHT | pygame.K_l:
                        return SelectState(
                            self.towers,
                            False,
                            (self.selected_tower + 1) % len(self.towers),
                        )
                    case pygame.K_F1:
                        return HelpState(
                            self.towers, False, "a - Move left ; d - Move right ;"
                        )
        return self


@dataclass()
class SolveState(GameState):
    def poll(self):
        print("SolveState", self.towers)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        return GameState(self.towers, False)
                    case pygame.K_r:
                        return RecursiveSolveState(
                            self.fresh_towers(),
                            False,
                            GameState(self.fresh_towers(), False).hanoi_recursive(),
                        )
                    case pygame.K_i:
                        return IterativeSolveState(
                            self.fresh_towers(),
                            False,
                            GameState(self.fresh_towers(), False).hanoi_iterative(),
                        )
                    case pygame.K_F1:
                        return HelpState(
                            self.towers,
                            False,
                            "r - Recursive solve ; i - Iterative solve ;",
                        )
        return self


@dataclass()
class RecursiveSolveState(GameState):
    history: list[GameState]

    def poll(self):
        print("RecursiveSolveState", self.towers)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE | pygame.K_SPACE:
                        return GameState(self.towers, False)
        return self

    def next(self):
        # pygame.time.wait(1000)
        if len(self.history) == 0:
            return GameState(self.towers, False)
        return RecursiveSolveState(self.history[0].towers, False, self.history[1:])


@dataclass()
class IterativeSolveState(GameState):
    history: list[GameState]

    def poll(self):
        print("IterativeSolveState", self.towers)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE | pygame.K_SPACE:
                        return GameState(self.towers, False)
        return self

    def next(self):
        # pygame.time.wait(1000)
        if len(self.history) == 0:
            return GameState(self.towers, False)
        return IterativeSolveState(self.history[0].towers, False, self.history[1:])


@dataclass()
class MoveState(GameState):
    selected_tower: int

    def poll(self):
        print("MoveState", self.selected_tower, self.towers)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        return GameState(self.towers, False)
                    case pygame.K_SPACE:
                        if len(self.towers[self.selected_tower].disks) == 0:
                            return self
                        return SelectState(self.towers, False, self.selected_tower)
                    case pygame.K_a | pygame.K_LEFT | pygame.K_h:
                        return MoveState(
                            self.towers,
                            False,
                            (self.selected_tower - 1) % len(self.towers),
                        )
                    case pygame.K_d | pygame.K_RIGHT | pygame.K_l:
                        return MoveState(
                            self.towers,
                            False,
                            (self.selected_tower + 1) % len(self.towers),
                        )
                    case pygame.K_F1:
                        return HelpState(
                            self.towers,
                            False,
                            "space - Select ; left - Move left ; right - Move right ;",
                        )
        return self
