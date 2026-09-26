[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# game-performance-75

`game-performance-75` is a lightweight Python-based telemetry library designed to monitor, log, and analyze real-time frame rates and hardware utilization for PC games. It provides game developers and hardware testers with actionable performance insights, specifically optimized for targets like stable 75 FPS gaming on high-refresh-rate monitors.

## Features

* **Real-time Telemetry Logging**: Captures raw frame times, CPU/GPU temperatures, and VRAM overhead on a millisecond-precision interval.
* **Micro-Stutter Detection**: Automatically flags frame drops below the 75 FPS target and calculates 1% low metrics.
* **Zero-overhead Architecture**: Runs on a background thread using asynchronous I/O to ensure the monitoring process does not degrade game engine performance.
* **Portable Reports**: Exports session telemetry to structured JSON or CSV files for post-match analysis.

## Installation

Install the package and its hardware telemetry dependencies via pip:

```bash
pip install game-performance-75
```

Note: Windows users may need to run this command in an administrator terminal to allow the CPU temperature probes to bind correctly.

## Usage

A basic example of monitoring a game session and extracting performance metrics:

```python
import time
from gp75 import SessionMonitor

# Initialize the monitor targeting a 75 FPS baseline
monitor = SessionMonitor(target_fps=75, sample_rate_ms=10)

print("Starting performance tracking...")
monitor.start_session()

# Simulate your game loop
for frame in range(500):
    time.sleep(0.0133) # Simulate ~75 FPS frame pacing
    monitor.tick()

# End telemetry and export data
session_results = monitor.end_session(export_path="game_results.json")

print(f"Session Complete!")
print(f"Average FPS: {session_results['avg_fps']:.2f}")
print(f"Time spent below 75 FPS: {session_results['pct_below_target']}%")
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.