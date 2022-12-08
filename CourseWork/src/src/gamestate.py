from collections.abc import Callable
from dataclasses import dataclass
from random import randint
from math import log

import pygame

from . import ptext

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
                            "s - Solve mode\nm - Move mode\nr - Restart game\nF1 - Help menu\nt - Change tower count\nd - Change disk count\nq - Quit",
                            self,
                        )
                    case pygame.K_t:
                        return ChangeTowerCountState(self.towers, False)
                    case pygame.K_d:
                        return ChangeDiskCountState(self.towers, False)
                    case pygame.K_q:
                        return GameState(self.towers, True)
        return self

    def render(self) -> None:
        backgroud_color = pygame.Color((130, 130, 130))
        screen_size = Size(1920, 1080)
        window = pygame.display.set_mode(screen_size)
        window.fill(backgroud_color)
        tower_color = pygame.Color((200, 50, 50))
        disk_color = pygame.Color((50, 200, 50))
        max_disks = self.total_disks()
        first_tower_x = screen_size.width / len(self.towers) / 3
        max_width_disk = 2 * first_tower_x
        towers_rects: list[pygame.Rect] = []
        disks_rects: list[pygame.Rect] = []
        for i, tower in enumerate(self.towers):
            tower_size = Size(
                max_width_disk / log(max_disks + 1, 2), screen_size.height
            )
            tower_position = Position(
                first_tower_x + screen_size.width / len(self.towers) * i,
                0,
            )
            center_of_tower = Position(
                tower_position.x + tower_size.width / 2, tower_position.y
            )
            towers_rects.append(
                tower.draw(
                    tower_position,
                    tower_size,
                )
            )
            for j, disk in enumerate(tower.disks):
                disk_size = Size(
                    max_width_disk / log(max_disks + 1, disk.weight + 1),
                    screen_size.height / max_disks,
                )
                disk_position = Position(
                    center_of_tower.x - disk_size.width / 2,
                    screen_size.height - disk_size.height * (j + 1),
                )
                disks_rects.append(disk.draw(disk_position, disk_size))
        for tower in towers_rects:
            pygame.draw.rect(window, tower_color, tower)
        for disk in disks_rects:
            pygame.draw.rect(window, disk_color, disk)

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
            self.total_disks(), 0, len(self.towers) - 1, 1
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

        disks: int = self.total_disks()
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
        return (
            len(self.towers) > 1
            and self.towers[from_tower].can_pop()
            and self.towers[to_tower].can_push(self.towers[from_tower].last())
        )

    def total_disks(self) -> int:
        return len(flat_map(lambda id: id, map(lambda tower: tower.disks, self.towers)))

    def fresh_towers(self, disks) -> list[Tower]:
        towers: list[Tower] = list(map(lambda _: Tower([]), range(len(self.towers))))
        towers[0].disks = list(map(lambda x: Disk(x), range(disks, 0, -1)))
        return towers

    def log(self) -> str:
        return ""


@dataclass()
class ChangeDiskCountState(GameState):
    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        return GameState(self.towers, False)
                    case pygame.K_p:
                        return ChangeDiskCountState(
                            self.fresh_towers(self.total_disks() + 1), False
                        )
                    case pygame.K_m:
                        if self.total_disks() == 1:
                            return self
                        return ChangeDiskCountState(
                            self.fresh_towers(self.total_disks() - 1), False
                        )
                    case pygame.K_F1:
                        return HelpState(
                            self.towers,
                            False,
                            "Any change restarts the game!\np - Increase number of disks\nm - Decrease number of disks\nESC - Go back",
                            self,
                        )
        return self


@dataclass()
class ChangeTowerCountState(GameState):
    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        return GameState(self.towers, False)
                    case pygame.K_p:
                        return ChangeTowerCountState(
                            self.fresh_towers(self.total_disks()) + [Tower([])], False
                        )
                    case pygame.K_m:
                        if len(self.towers) == 1:
                            return self
                        return ChangeTowerCountState(
                            self.fresh_towers(self.total_disks())[:-1], False
                        )
                    case pygame.K_F1:
                        return HelpState(
                            self.towers,
                            False,
                            "Any change restarts the game!\np - Increase number of towers\nm - Decrease number of towers\nESC - Go back",
                            self,
                        )
        return self


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
                        return GameState(self.fresh_towers(self.total_disks()), False)
                    case pygame.K_F1:
                        return HelpState(
                            self.towers,
                            False,
                            "Do you wanna restart?\ny - YES\nn, ESC, Space - NO, go back",
                            self,
                        )
        return self


@dataclass()
class HelpState(GameState):
    help_text: str
    caller: GameState

    def log(self) -> str:
        return f"{self.help_text} {self.caller.__class__.__name__}"

    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE | pygame.K_SPACE:
                        return self.caller
        return self

    def render(self):
        screen_size = Size(1920, 1080)
        super().render()
        ptext.draw(
            self.help_text,
            centerx=screen_size.width / 2,
            centery=screen_size.height / 2,
            fontsize=64,
            color=pygame.color.Color(0, 0, 0),
        )


@dataclass()
class SelectState(GameState):
    selected_tower: int
    to_tower: int

    def log(self) -> str:
        return f"{self.selected_tower} to {self.to_tower}"

    def render(self) -> None:
        backgroud_color = pygame.Color((130, 130, 130))
        screen_size = Size(1920, 1080)
        window = pygame.display.set_mode(screen_size)
        window.fill(backgroud_color)
        tower_color = pygame.Color((200, 50, 50))
        disk_color = pygame.Color((50, 200, 50))
        max_disks = self.total_disks()
        first_tower_x = screen_size.width / len(self.towers) / 3
        max_width_disk = 2 * first_tower_x
        towers_rects: list[pygame.Rect] = []
        disks_rects: list[pygame.Rect] = []
        for i, tower in enumerate(self.towers):
            tower_size = Size(
                max_width_disk / log(max_disks + 1, 2), screen_size.height
            )
            tower_position = Position(
                first_tower_x + screen_size.width / len(self.towers) * i,
                0,
            )
            center_of_tower = Position(
                tower_position.x + tower_size.width / 2, tower_position.y
            )
            towers_rects.append(
                tower.draw(
                    tower_position,
                    tower_size,
                )
            )
            for j, disk in enumerate(tower.disks):
                disk_size = Size(
                    max_width_disk / log(max_disks + 1, disk.weight + 1),
                    screen_size.height / max_disks,
                )
                disk_position = Position(
                    center_of_tower.x - disk_size.width / 2,
                    screen_size.height - disk_size.height * (j + 1),
                )
                disks_rects.append(disk.draw(disk_position, disk_size))
        for i, tower in enumerate(towers_rects):
            if i == self.selected_tower:
                pygame.draw.rect(window, pygame.Color(20, 20, 123), tower)
            elif i == self.to_tower:
                pygame.draw.rect(window, pygame.Color(20, 123, 123), tower)
            else:
                pygame.draw.rect(window, tower_color, tower)
        for disk in disks_rects:
            pygame.draw.rect(window, disk_color, disk)

    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_SPACE:
                        return MoveState(
                            self.move(self.selected_tower, self.to_tower).towers,
                            False,
                            self.to_tower,
                        )
                    case pygame.K_a | pygame.K_LEFT | pygame.K_h:
                        return SelectState(
                            self.towers,
                            False,
                            self.selected_tower,
                            (self.to_tower - 1) % len(self.towers),
                        )
                    case pygame.K_d | pygame.K_RIGHT | pygame.K_l:
                        return SelectState(
                            self.towers,
                            False,
                            self.selected_tower,
                            (self.to_tower + 1) % len(self.towers),
                        )
                    case pygame.K_F1:
                        return HelpState(
                            self.towers,
                            False,
                            "a - Move left\nd - Move right\nSPACE - select disk",
                            self,
                        )
        return self


@dataclass()
class SolveState(GameState):
    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        return GameState(self.towers, False)
                    case pygame.K_r:
                        return RecursiveSolveState(
                            self.fresh_towers(self.total_disks()),
                            False,
                            GameState(
                                self.fresh_towers(self.total_disks()), False
                            ).hanoi_recursive(),
                        )
                    case pygame.K_i:
                        return IterativeSolveState(
                            self.fresh_towers(self.total_disks()),
                            False,
                            GameState(
                                self.fresh_towers(self.total_disks()), False
                            ).hanoi_iterative(),
                        )
                    case pygame.K_F1:
                        return HelpState(
                            self.towers,
                            False,
                            "r - Recursive solve\ni - Iterative solve\nESC - Go back\nF1 - Help menu",
                            self,
                        )
        return self


@dataclass()
class RecursiveSolveState(GameState):
    history: list[GameState]

    def log(self) -> str:
        return f"{self.history}"

    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE | pygame.K_SPACE:
                        return GameState(self.towers, False)
        return self

    def next(self):
        pygame.time.wait(1000)
        if len(self.history) == 0:
            return RestartState(self.towers, False)
        return RecursiveSolveState(self.history[0].towers, False, self.history[1:])


@dataclass()
class IterativeSolveState(GameState):
    history: list[GameState]

    def log(self) -> str:
        return f"{self.history}"

    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState(self.towers, True)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE | pygame.K_SPACE:
                        return GameState(self.towers, False)
        return self

    def next(self):
        pygame.time.wait(1000)
        if len(self.history) == 0:
            return RestartState(self.towers, False)
        return IterativeSolveState(self.history[0].towers, False, self.history[1:])


@dataclass()
class MoveState(GameState):
    selected_tower: int

    def log(self) -> str:
        return f"{self.selected_tower}"

    def render(self) -> None:
        backgroud_color = pygame.Color((130, 130, 130))
        screen_size = Size(1920, 1080)
        window = pygame.display.set_mode(screen_size)
        window.fill(backgroud_color)
        tower_color = pygame.Color((200, 50, 50))
        disk_color = pygame.Color((50, 200, 50))
        max_disks = self.total_disks()
        first_tower_x = screen_size.width / len(self.towers) / 3
        max_width_disk = 2 * first_tower_x
        towers_rects: list[pygame.Rect] = []
        disks_rects: list[pygame.Rect] = []
        for i, tower in enumerate(self.towers):
            tower_size = Size(
                max_width_disk / log(max_disks + 1, 2), screen_size.height
            )
            tower_position = Position(
                first_tower_x + screen_size.width / len(self.towers) * i,
                0,
            )
            center_of_tower = Position(
                tower_position.x + tower_size.width / 2, tower_position.y
            )
            towers_rects.append(
                tower.draw(
                    tower_position,
                    tower_size,
                )
            )
            for j, disk in enumerate(tower.disks):
                disk_size = Size(
                    max_width_disk / log(max_disks + 1, disk.weight + 1),
                    screen_size.height / max_disks,
                )
                disk_position = Position(
                    center_of_tower.x - disk_size.width / 2,
                    screen_size.height - disk_size.height * (j + 1),
                )
                disks_rects.append(disk.draw(disk_position, disk_size))
        for i, tower in enumerate(towers_rects):
            if i == self.selected_tower:
                pygame.draw.rect(window, pygame.Color(20, 20, 123), tower)
            else:
                pygame.draw.rect(window, tower_color, tower)
        for disk in disks_rects:
            pygame.draw.rect(window, disk_color, disk)

    def poll(self):
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
                        return SelectState(
                            self.towers, False, self.selected_tower, self.selected_tower
                        )
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
                            "space - Select\nleft - Move left\nright - Move right",
                            self,
                        )
        return self
