import random
import time
import functools
from typing import Callable, Any, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

class NetworkLootDropError(Exception):
    """Raised when network telemetry packet fails to transmit after full retries."""
    pass

def retry_network_op(
    max_attempts: int = 4,
    base_delay_ms: float = 16.67,
    backoff_multiplier: float = 2.0,
    jitter: bool = True
) -> Callable[[F], F]:
    """
    Decorator providing exponential frame-aligned backoff for game network calls.
    Paces retries around 60 FPS frame budgets with optional packet jitter.
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            current_delay = base_delay_ms / 1000.0
            
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise NetworkLootDropError(
                            f"Telemetry drop after {attempts} frame ticks: {exc}"
                        ) from exc
                    
                    sleep_time = current_delay
                    if jitter:
                        sleep_time *= (0.8 + random.random() * 0.4)
                    
                    time.sleep(sleep_time)
                    current_delay *= backoff_multiplier
                    
        return wrapper  # type: ignore
    return decorator

def transmit_match_telemetry(endpoint: str, payload: dict) -> bool:
    """Sample network operation utilizing frame-aware retries."""
    @retry_network_op(max_attempts=3, base_delay_ms=33.33)
    def _send():
        if random.random() < 0.5:
            raise ConnectionResetError("Packet lost on server tick boundary")
        return True

    return _send()