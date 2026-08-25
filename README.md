# game-performance-75

game-performance-75 is a Python library that profiles game loops to diagnose performance issues and maintain stable frame rates. It focuses on helping developers reach and sustain 75 FPS in their Python-based games through targeted optimizations.

## Features

- Precise frame timing measurement with support for variable refresh rates
- Identification of expensive functions in the game loop using built-in profilers
- Memory allocation tracking to spot leaks during extended play sessions
- Generation of visual reports including FPS graphs and bottleneck heatmaps

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Developer/game-performance-75.git
cd game-performance-75
pip install -r requirements.txt
```

## Usage

Add profiling to your game like this:

```python
from game_performance_75 import GameProfiler

profiler = GameProfiler(target_fps=75)
profiler.begin_session()

# Main game loop
while True:
    profiler.frame_start()
    # Update and render
    profiler.frame_end()

profiler.end_session()
profiler.export_report("report.html")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)