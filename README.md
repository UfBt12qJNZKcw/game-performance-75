# game-performance-75

`game-performance-75` is a high-precision telemetry and optimization toolkit designed to monitor frame stability and CPU/GPU bottlenecks in real-time. This utility provides Python-based developers with granular insights into engine-level resource consumption during intense gaming sessions.

## Features

*   **Latency Profiling:** Measures frame-time variance with sub-millisecond accuracy to identify micro-stuttering causes.
*   **Thermal Throttling Detection:** Automatically flags performance drops triggered by hardware temperature spikes.
*   **Process Priority Injection:** Optimizes Windows/Linux thread scheduling for the active game process to reduce input latency.
*   **CSV Export Engine:** Generates structured performance logs for comparative analysis across different hardware configurations.

## Installation

Ensure you have Python 3.9+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/game-performance-75.git
cd game-performance-75
pip install -r requirements.txt
```

## Usage

To monitor a specific game process by its PID, run the following command:

```python
from monitor import PerformanceEngine

# Initialize the engine for the target process
engine = PerformanceEngine(pid=1234)

# Start tracking and log results to ./logs/session_01.csv
engine.start_tracking(output="session_01.csv", interval=0.5)
```

For a CLI-based quick look at system-wide impact, use the integrated diagnostic tool:

```bash
python monitor.py --live --threshold 60
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.