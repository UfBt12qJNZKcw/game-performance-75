import logging
import json

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(f'{name}.log')
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


def log_game_event(logger, event_type, data):
    if not isinstance(event_type, str) or len(event_type) == 0:
        logger.error('Invalid event_type provided')
        return
    if not isinstance(data, dict):
        logger.error('Data must be a dictionary')
        return

    logger.info('Logging game event: %s', event_type)
    logger.info('Event data: %s', json.dumps(data))


if __name__ == '__main__':
    my_logger = setup_logger('game_events')
    log_game_event(my_logger, 'player_score', {'player_id': 123, 'score': 456})
    log_game_event(my_logger, '', {'player_id': 124})
    log_game_event(my_logger, 'player_action', 'not_a_dict')