def hanoi(ndisks: int, startPeg: int = 1, endPeg: int = 3) -> None:
    if ndisks:
        hanoi(ndisks - 1, startPeg, 6 - startPeg - endPeg)
        print(f"Move disk {ndisks} from peg {startPeg} to peg {endPeg}")
        hanoi(ndisks - 1, 6 - startPeg - endPeg, endPeg)
