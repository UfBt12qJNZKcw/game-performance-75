import time
import os
import json

class Logger:
    def __init__(self, log_file='game.log'):
        self.log_file = log_file
        self.start_time = time.time()
        self.ensure_log_file_exists()

    def ensure_log_file_exists(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write(json.dumps([]))

    def log(self, message):
        elapsed_time = time.time() - self.start_time
        log_entry = {'time': elapsed_time, 'message': message}
        self.write_log(log_entry)

    def write_log(self, log_entry):
        with open(self.log_file, 'r+') as f:
            logs = json.load(f)
            logs.append(log_entry)
            f.seek(0)
            json.dump(logs, f)

    def get_logs(self):
        with open(self.log_file, 'r') as f:
            return json.load(f)

    def clear_logs(self):
        with open(self.log_file, 'w') as f:
            f.write(json.dumps([]))

logger = Logger()  # Global logger instance
logger.log('Game started')

# Example usage
if __name__ == '__main__':
    logger.log('Initializing game components')
    logs = logger.get_logs()
    print(logs)