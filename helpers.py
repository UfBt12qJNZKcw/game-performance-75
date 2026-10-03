import time
import random
from typing import Callable, Any, Generator

def chaos_backoff(base_delay: float, max_delay: float, factor: float = 1.5) -> Generator[float, float, None]:
    """Yields exponentially increasing delays with dynamic jitter steered by feedback."""
    delay = base_delay
    while True:
        feedback = yield delay
        scale = feedback if feedback is not None else 1.0
        jitter = random.uniform(0.5, 1.5) * scale
        delay = min(delay * factor * jitter, max_delay)

def resilient_retry(retries: int = 3, base_delay: float = 0.1, max_delay: float = 2.0):
    """
    Decorator applying a chaotic backoff retry strategy.
    Uses exception entropy to prevent synchronized packet storms in game clients.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            backoff_gen = chaos_backoff(base_delay, max_delay)
            next_delay = next(backoff_gen)
            
            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    if attempt == retries:
                        raise exc
                    
                    # Derive dynamic entropy from the exception string to guide backoff
                    entropy = (hash(str(exc)) % 100) / 100.0
                    time.sleep(next_delay)
                    next_delay = backoff_gen.send(1.0 + entropy)
        return wrapper
    return decorator
