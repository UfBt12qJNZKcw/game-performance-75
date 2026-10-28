# game-performance-75

`game-performance-75` is a high-performance Python toolkit designed to monitor and optimize system resources during intense gaming sessions. It provides real-time telemetry tracking and automated background process prioritization to ensure stable frame rates.

## Features
* **Adaptive Resource Manager:** Dynamically lowers the priority of non-essential background tasks when high GPU/CPU usage is detected.
* **Telemetry Overlay:** Real-time logging of frametimes, thermal data, and RAM consumption saved to local CSV files for benchmarking.
* **Smart Throttle Protection:** Monitors CPU frequency and temperature, offering early warnings or automated power limit adjustments to prevent thermal throttling.
* **One-Click Optimization:** Includes a pre-configured sweep mode to clear volatile cache directories and background stale services before launching games.

## Installation

Ensure you have Python 3.8+ installed. It is recommended to run this tool within a virtual environment.

```bash
# Clone the repository
git clone https://github.com/Developer/game-performance-75.git
cd game-performance-75

# Install dependencies
pip install -r requirements.txt
```

## Usage

To start the performance monitor and generate a live log of your system state, use the following command:

```bash
python main.py --monitor --interval 1000
```

To run a full optimization sweep before launching your game:

```bash
python main.py --optimize --launch "path/to/game.exe"
```

The tool will default to standard reporting mode if no arguments are provided. Check `config.json` to customize notification thresholds for thermal spikes.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.