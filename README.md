# game-performance-75

`game-performance-75` is a high-precision telemetry and optimization toolkit designed to monitor hardware utilization and framerate stability in Python-based game environments. This project provides real-time performance logging and automated resource allocation to minimize stuttering during heavy gaming sessions.

## Features

*   **FPS Telemetry:** Captures sub-millisecond frame time data with minimal CPU overhead.
*   **Dynamic Resource Throttling:** Automatically adjusts background process priority during high-demand gameplay.
*   **Thermal Monitoring:** Tracks GPU and CPU junction temperatures, logging anomalies to a local CSV report.
*   **Overlay Integration:** Provides a lightweight CLI output compatible with standard windowed game hooks.

## Installation

Ensure you have Python 3.8+ installed. You can install the package directly via pip:

```bash
git clone https://github.com/Developer/game-performance-75.git
cd game-performance-75
pip install -r requirements.txt
python setup.py install
```

## Usage

To initialize the performance monitor for a specific executable process, use the following command:

```python
from game_perf import Monitor

# Initialize monitor on target process ID
monitor = Monitor(pid=1234, sample_rate=0.5)

# Start logging performance to disk
monitor.start_log(output_file="session_stats.csv")

# Run optimization cycle
monitor.optimize()
```

The tool will now continuously track frame delivery and hardware thermal states, outputting alerts if the system temperature exceeds 85°C.

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.