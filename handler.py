import time
import random
import functools
from typing import Callable, Any

class NetworkSyncError(Exception):
    """Raised when game telemetry or network payload fails to transmit."""
    pass

def frame_aware_retry(
    max_retries: int = 4,
    base_delay_ms: float = 16.67,
    max_delay_ms: float = 500.0,
    jitter_factor: float = 0.25
) -> Callable:
    """Decorator for network operations scaling delay with frame timing."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            current_delay = base_delay_ms / 1000.0
            
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    attempts += 1
                    if attempts > max_retries:
                        raise NetworkSyncError(
                            f"Network dispatch failed after {max_retries} frame-budgeted attempts"
                        ) from exc
                    
                    jitter = random.uniform(1.0 - jitter_factor, 1.0 + jitter_factor)
                    sleep_time = min(current_delay * (2 ** (attempts - 1)) * jitter, max_delay_ms / 1000.0)
                    time.sleep(sleep_time)
                    current_delay *= 1.5
        return wrapper
    return decorator

class TelemetryDispatcher:
    def __init__(self, endpoint_url: str):
        self.endpoint_url = endpoint_url
        self.packets_sent = 0

    @frame_aware_retry(max_retries=3, base_delay_ms=33.33)
    def transmit_frame_stats(self, frame_id: int, fps: float, ping_ms: float) -> bool:
        if random.random() < 0.4:
            raise ConnectionResetError("Packet dropped on socket write")
        self.packets_sent += 1
        return True
