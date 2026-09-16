[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# game-performance-75

`game-performance-75` is a lightweight Python telemetry tool designed to capture frame time consistency and hardware resource utilization during active gaming sessions. It analyzes real-time system metrics to help gamers pinpoint micro-stutter, evaluate 75 FPS performance targets, and optimize graphics configurations.

## Features

- **Frame Time & Lows Tracking**: Logs 1% and 0.1% low FPS metrics alongside hardware telemetry to accurately reflect perceived smoothness.
- **Stutter Detection Algorithm**: Flags any render frame times exceeding the 13.33ms baseline window required for stable 75Hz display output.
- **Automated Visual Reports**: Generates HTML performance summaries with interactive matplotlib plots showing CPU/GPU temperature and clock speed correlation.
- **Low-Overhead Execution**: Runs as an asynchronous background process with sub-1% CPU usage, preventing benchmark skewing.

## Installation

Ensure you have Python 3.9+ installed, then run:

```bash
git clone https://github.com/Developer/game-performance-75.git
cd game-performance-75
pip install -r requirements.txt
python setup.py install
```

## Quick Start

Start a session recorder in your Python script or integrate it into your automated benchmarks:

```python
from game_perf75 import TelemetryMonitor, ReportGenerator

# Initialize monitor tuned for a 75 FPS baseline target
monitor = TelemetryMonitor(target_fps=75, sampling_rate_ms=100)

# Start logging during gameplay
monitor.start("Cyberpunk2077_HighSettings")

# ... run your game or benchmark loop ...

# Stop logging and build the HTML report
log_path = monitor.stop()
report = ReportGenerator(log_path)
report.to_html("performance_summary.html")
```

To run directly from the command line:

```bash
python -m game_perf75 --duration 300 --output session_log.json
```

## License

Distributed under the MIT License. See `LICENSE` for details.