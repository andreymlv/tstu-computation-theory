def hanoi_recursive(
    disks: int, source: int, target: int, temp: int
) -> list[tuple[int, int]]:
    """
    Usage: hanoi_recursive(number of disks, from, to, temp)
    Returns: list of moves [(from, to), (from, to), ...]
    """
    if disks == 0:
        return []
    return (
        hanoi_recursive(disks - 1, source, temp, target)
        + [(source, target)]
        + hanoi_recursive(disks - 1, temp, target, source)
    )
