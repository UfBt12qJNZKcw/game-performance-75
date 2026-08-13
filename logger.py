import logging
import os

class PerformanceLogger:
    def __init__(self, log_file='performance.log'):
        self.logger = logging.getLogger('PerformanceLogger')
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(os.path.join(os.getcwd(), log_file))
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_metric(self, metric_name, value, context=''):
        self.logger.info(f'{metric_name}: {value} | Context: {context}')
        
    def log_error(self, error_message, context=''):
        self.logger.error(f'Error: {error_message} | Context: {context}') 

    def log_warning(self, warning_message, context=''):
        self.logger.warning(f'Warning: {warning_message} | Context: {context}') 

performance_logger = PerformanceLogger()

# Example of logging performance metrics
performance_logger.log_metric('FPS', 60, 'Main Game Loop')
performance_logger.log_warning('High Latency Detected', 'Network Module')
performance_logger.log_error('Failed to load texture', 'Asset Loader')