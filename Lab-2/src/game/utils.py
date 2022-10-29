from os import popen, system, name

if name == "nt":
    from msvcrt import kbhit, getch
else:
    from sys import stdin
    from termios import tcflush, TCIOFLUSH


def dimensions() -> tuple[int, int]:
    """Calls OS-specific functions to get dimensions of terminal.

    :return: tuple that contains width and height dimensions of terminal.
    """
    width = popen("tput cols", "r").readline()
    height = popen("tput lines", "r").readline()
    return int(width), int(height)


def clear_screen() -> None:
    system("cls" if name == "nt" else "clear")


def flush_input():
    if name == "nt":
        while kbhit():
            getch()
    else:
        tcflush(stdin, TCIOFLUSH)
