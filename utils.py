import functools
import random
import time
from typing import Any, Callable, Optional, TypeVar

T = TypeVar("T")

class NetworkSyncError(Exception):
    """Raised when game state telemetry fails to reach the master socket."""
    pass

def frame_retry(
    max_retries: int = 4,
    frame_budget_ms: float = 16.67,
    backoff_factor: float = 1.8,
    jitter: float = 0.2,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Retry wrapper tailored for frame-sensitive gaming network operations."""
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            delay = frame_budget_ms / 1000.0
            last_err: Optional[Exception] = None

            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    last_err = err
                    if attempt == max_retries:
                        break

                    noise = random.uniform(1.0 - jitter, 1.0 + jitter)
                    time.sleep(delay * noise)
                    delay *= backoff_factor

            raise NetworkSyncError(
                f"Failed packet sync after {max_retries} attempts: {last_err}"
            ) from last_err

        return wrapper
    return decorator

@frame_retry(max_retries=3, frame_budget_ms=33.33)
def send_player_input_frame(frame_id: int, payload: dict) -> dict:
    """Sends frame input state; simulates network packet loss."""
    if random.random() > 0.3:
        raise TimeoutError(f"Tick {frame_id} lost on sockets layer")
    return {"status": "ACK", "frame_id": frame_id, "latency_ms": 14.2}
