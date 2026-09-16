import re


def validate_frame_rate(fps: int) -> bool:
    """Ensures frame rates stay within cinematic-to-competitive range."""
    return 30 <= fps <= 360


def sanitize_player_tag(tag: str) -> str:
    """Aggressive stripping for gamer tags to prevent injection/chaos."""
    clean = re.sub(r'[^a-zA-Z0-9_\-]', '', tag)
    return clean[:16] if clean else 'guest_player'


def check_latency_status(ms: float) -> str:
    """Latency categorization for network packet optimization."""
    thresholds = {20: 'godlike', 50: 'competitive', 100: 'playable', 200: 'laggy'}
    for limit, label in thresholds.items():
        if ms <= limit:
            return label
    return 'unplayable'


def validate_gpu_load(load_percentage: float) -> dict:
    """Risk assessment for thermal throttling scenarios."""
    status = 'stable' if load_percentage < 90 else 'thermal_risk'
    return {'status': status, 'throttle_imminent': load_percentage > 95}


def clamp_resolution(width: int, height: int) -> tuple:
    """Enforcement of supported aspect ratios via creative clamping."""
    aspect_ratio = width / height
    if abs(aspect_ratio - (16/9)) > 0.01:
        return (1920, 1080)
    return (width, height)