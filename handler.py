import random
from typing import List, Dict, Any

def game_event_trigger(player_id: int, event_type: str, event_data: Dict[str, Any]) -> None:
    """
    Triggers a game event for a player.

    Parameters:
    player_id (int): Unique identifier for the player.
    event_type (str): The type of event to trigger.
    event_data (Dict[str, Any]): Additional data related to the event.
    """
    print(f"Triggering {event_type} for player {player_id} with data: {event_data}")


def generate_random_loot(player_id: int) -> List[str]:
    """
    Generates a list of random loot items for the player.

    Parameters:
    player_id (int): Unique identifier for the player.

    Returns:
    List[str]: List of loot items obtained by the player.
    """
    loot_items = ['Sword', 'Shield', 'Potion', 'Gold', 'Armor']
    num_loot = random.randint(1, 3)
    obtained_loot = random.sample(loot_items, num_loot)
    print(f"Player {player_id} obtained loot: {obtained_loot}")
    return obtained_loot


def handle_player_action(player_id: int, action: str) -> None:
    """
    Handles an action performed by the player.

    Parameters:
    player_id (int): Unique identifier for the player.
    action (str): The action to be handled.
    """
    print(f"Player {player_id} performed action: {action}")
    if action == 'loot':
        loot = generate_random_loot(player_id)
        game_event_trigger(player_id, 'loot', {'items': loot})
    elif action == 'attack':
        game_event_trigger(player_id, 'attack', {'damage': random.randint(5, 15)})

