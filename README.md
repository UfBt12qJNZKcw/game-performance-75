# game-performance-75

`game-performance-75` is a high-performance Python toolkit designed to monitor and optimize system resources during intense gaming sessions. It provides real-time telemetry to identify bottlenecks and automate background process suspension for maximum frame rate stability.

## Features

*   **Process Priority Orchestration:** Automatically elevates the priority of your active game process while throttling background non-essential applications.
*   **Hardware Telemetry:** Aggregates CPU, GPU, and RAM usage data via `psutil` to generate low-latency performance overlays.
*   **Thermal Throttling Protection:** Triggers configurable alerts and system cooling profiles when hardware temperatures exceed safety thresholds.
*   **Game Mode Automation:** Detects active full-screen applications and applies pre-defined power profiles without requiring manual input.

## Installation

Ensure you have Python 3.8+ installed. It is recommended to use a virtual environment:

```bash
# Clone the repository
git clone https://github.com/Developer/game-performance-75.git
cd game-performance-75

# Install dependencies
pip install -r requirements.txt
```

## Basic Usage

Run the monitor script with administrative privileges to allow the tool to manage system process priorities:

```bash
# Execute with elevated permissions
sudo python3 main.py --target "game_executable_name.exe" --interval 1.0
```

To run the monitor in background mode and log performance metrics to a CSV file:

```bash
python3 main.py --log output.csv --daemon
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.