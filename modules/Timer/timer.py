import time


class Timer:
    previous_time = None

    def __init__(self) -> None:
        self.previous_time = time.perf_counter()

    def step(self) -> float:
        delta: float = time.perf_counter() - self.previous_time
        self.previous_time = time.perf_counter()
        if delta > 1:
            return 0.0
        else:
            return delta
