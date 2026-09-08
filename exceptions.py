class PerformanceValidationError(ValueError):
    """Custom exception raised when game metrics violate performance baselines."""
    def __init__(self, metric: str, value: float, limit: float, operator: str):
        self.metric = metric
        self.value = value
        self.limit = limit
        self.operator = operator
        super().__init__(f"Metric '{metric}' failed validation: {value} {operator} {limit}")


def validate_loop_inputs(metrics: dict[str, float]) -> None:
    """Validates real-time performance telemetry inputs using a creative validation map."""
    thresholds = {
        "fps": (1.0, 1000.0),
        "frame_time_ms": (0.0, 100.0),
        "jitter_ms": (0.0, 50.0),
    }
    
    for key, value in metrics.items():
        if key in thresholds:
            min_val, max_val = thresholds[key]
            if not (min_val <= value <= max_val):
                raise PerformanceValidationError(
                    metric=key,
                    value=value,
                    limit=max_val if value > max_val else min_val,
                    operator="<=" if value > max_val else ">="
                )