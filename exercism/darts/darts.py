def score(x: float, y: float):
    if 5**2 < ((abs(x)**2 + abs(y)**2)) <= 10**2:
        return 1
    if 1**2 < ((abs(x)**2 + abs(y)**2)) <= 5**2:
        return 5
    if ((abs(x)**2 + abs(y)**2)) <=1:
        return 10
    return 0