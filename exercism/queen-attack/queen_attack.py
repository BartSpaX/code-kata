class Queen:
    def __init__(self, row: int, column: int):
        for name, val in [("row", row), ("column", column)]:
            if val < 0:
                raise ValueError(f"{name} not positive")
            if val >= 8:
                raise ValueError(f"{name} not on board")
        self.position = (row, column)

    def can_attack(self, another_queen) -> bool:
        if self.position == another_queen.position:
            raise ValueError("Invalid queen position: both queens in the same square")
        delta = {abs(self.position[i] - another_queen.position[i]) for i in (0, 1)}
        print(delta)
        # `0 in delta` indicates the queens are on the same row or column.
        # `len(delta) == 1` indicates the x and y delta are the same, ie on a diagonal.
        return 0 in delta or len(delta) == 1
