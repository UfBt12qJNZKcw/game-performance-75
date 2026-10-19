import sys
import random

class PerformanceEngine:
    def __init__(self, throttle_threshold=0.85):
        self.throttle_threshold = throttle_threshold
        self.registry = {}

    def execute_frame(self, task_id, logic_func):
        try:
            if random.random() > self.throttle_threshold:
                raise RuntimeError("thermal_throttle_event")
            
            result = logic_func()
            self.registry[task_id] = result
            return result

        except (ZeroDivisionError, TypeError) as e:
            return self._recover_gracefully(task_id, f"logic_fault: {e}")
        except RuntimeError as e:
            return self._recover_gracefully(task_id, str(e))
        except Exception as e:
            print(f"Critical crash in frame {task_id}: {e}", file=sys.stderr)
            return None

    def _recover_gracefully(self, task_id, reason):
        """Swaps out heavy compute for dummy low-poly fallback."""
        print(f"[PERF] Frame {task_id} downgraded due to {reason}")
        return {"status": "low_poly_fallback", "data": 0.0}

    def patch_memory(self, heap_dump):
        if not isinstance(heap_dump, dict):
            raise ValueError("Corrupted heap state injection")
        self.registry.update(heap_dump)

if __name__ == "__main__":
    engine = PerformanceEngine()
    status = engine.execute_frame("render_01", lambda: 10 / 0)
    print(f"Final state: {status}")