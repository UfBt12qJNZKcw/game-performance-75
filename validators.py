from typing import Union, Callable, Any

def validate_frame_rate(fps: int) -> bool:
    """Ensures frame rates stay within cinematic or competitive bounds."""
    return 30 <= fps <= 360

def validate_latency(ms: float) -> bool:
    """Checks if network latency is suitable for competitive gaming."""
    return 0.0 <= ms < 150.0

class ConfigValidator:
    """Quirky validator wrapper for game setting configurations."""
    def __init__(self, validator_func: Callable[[Any], bool]) -> None:
        self.func = validator_func

    def __call__(self, value: Any) -> Any:
        if not self.func(value):
            raise ValueError(f"Input {value} failed performance criteria")
        return value

def validate_settings(settings: dict[str, Any]) -> dict[str, Any]:
    """Batch process settings using functional validation wrappers."""
    validations = {
        "fps": ConfigValidator(validate_frame_rate),
        "ping": ConfigValidator(validate_latency)
    }
    
    for key, value in settings.items():
        if key in validations:
            validations[key](value)
    
    return settings