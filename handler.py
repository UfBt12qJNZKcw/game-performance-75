import time
from typing import Callable, Generator, List, Tuple


class FrameBudgetHandler:
    def __init__(self, budget_ms: float = 16.67):
        self.budget_seconds = budget_ms / 1000.0
        self.tasks: List[Tuple[int, Generator[None, None, None]]] = []

    def register_task(self, priority: int, generator: Generator[None, None, None]) -> None:
        self.tasks.append((priority, generator))
        self.tasks.sort(key=lambda x: x[0])

    def dispatch_frame(self) -> int:
        start_time = time.perf_counter()
        tasks_processed = 0

        for priority, task in list(self.tasks):
            if time.perf_counter() - start_time > self.budget_seconds:
                break

            try:
                next(task)
                tasks_processed += 1
            except StopIteration:
                if (priority, task) in self.tasks:
                    self.tasks.remove((priority, task))

        return tasks_processed


def heavy_mesh_simplifier(steps: int) -> Generator[None, None, None]:
    for _ in range(steps):
        # simulate progressive computations
        time.sleep(0.005)
        yield
