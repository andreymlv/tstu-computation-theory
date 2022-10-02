import os


def dimensions() -> tuple[int, int]:
    width = os.popen('tput cols', 'r').readline()
    height = os.popen('tput lines', 'r').readline()
    return int(width), int(height)


def clear_screen(lines: int) -> None:
    print('\n' * lines)
