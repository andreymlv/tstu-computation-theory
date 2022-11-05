def hanoi(disks: int, start_peg: int = 1, end_peg: int = 3) -> None:
    if disks:
        hanoi(disks - 1, start_peg, 6 - start_peg - end_peg)
        print(f"Move disk {disks} from peg {start_peg} to peg {end_peg}")
        hanoi(disks - 1, 6 - start_peg - end_peg, end_peg)
