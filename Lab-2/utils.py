import os


def dimensions() -> tuple[int, int]:
    """Calls OS-specific functions to get dimensions of terminal.

    :return: tuple that contains width and height dimensions of terminal.
    """
    width = os.popen('tput cols', 'r').readline()
    height = os.popen('tput lines', 'r').readline()
    return int(width), int(height)


def clear_screen() -> None:
    os.system('clear')


def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys
        import termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
