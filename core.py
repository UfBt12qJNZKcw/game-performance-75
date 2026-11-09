import sys
import time
from typing import Generator, List, Tuple


class RingBufferFramePool:
    """Lock-free ring buffer object pool for zero-allocation game state snapshots."""

    __slots__ = ("_buffer", "_capacity", "_head", "_tail", "_size", "_mask")

    def __init__(self, capacity_power_of_two: int = 1024):
        if not (capacity_power_of_two & (capacity_power_of_two - 1) == 0):
            raise ValueError("Capacity must be a power of two")
        self._capacity = capacity_power_of_two
        self._mask = capacity_power_of_two - 1
        self._buffer: List[List[float]] = [[0.0, 0.0, 0.0, 0.0] for _ in range(self._capacity)]
        self._head = 0
        self._tail = 0
        self._size = 0

    def push_transform(self, x: float, y: float, z: float, delta_time: float) -> bool:
        if self._size >= self._capacity:
            self._tail = (self._tail + 1) & self._mask
            self._size -= 1

        slot = self._buffer[self._head]
        slot[0] = x
        slot[1] = y
        slot[2] = z
        slot[3] = delta_time

        self._head = (self._head + 1) & self._mask
        self._size += 1
        return True

    def drain_batch(self, batch_size: int) -> Generator[Tuple[float, float, float, float], None, None]:
        count = min(batch_size, self._size)
        for _ in range(count):
            slot = self._buffer[self._tail]
            yield (slot[0], slot[1], slot[2], slot[3])
            self._tail = (self._tail + 1) & self._mask
            self._size -= 1

    @property
    def occupancy_ratio(self) -> float:
        return self._size / self._capacity
