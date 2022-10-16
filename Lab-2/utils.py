import os
import signal


def dimensions() -> tuple[int, int]:
    """Calls OS-specific functions to get dimensions of terminal.

    :return: tuple that contains width and height dimensions of terminal.
    """
    width = os.popen('tput cols', 'r').readline()
    height = os.popen('tput lines', 'r').readline()
    return int(width), int(height)


def clear_screen() -> None:
    os.system('cls||clear')


def get_char() -> str:
    return input('').split(" ")[0]


def handler(signum, frame):
    pass


def get_input(timeout=1) -> str:
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout)
    text: str = get_char()
    signal.alarm(0)
    return '' + text
