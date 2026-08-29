import json
def validate_game_input(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be dict")
    if "type" not in data or "value" not in data:
        raise ValueError("Missing type or value")
    if data["type"] not in ["score", "move", "hit"]:
        raise ValueError("Invalid input type")
    if not isinstance(data["value"], (int, float)) or data["value"] < 0:
        raise ValueError("Value must be non-negative number")
    return True
def main_processing_loop():
    raw_inputs = [{"type": "score", "value": 1500}, {"type": "move", "value": 42}, {"type": "invalid", "value": 10}, {"type": "hit", "value": -5}, {"type": "score", "value": "abc"}, {"type": "move", "value": 99}]
    processed_count = 0
    total_score = 0
    i = 0
    while i < len(raw_inputs):
        current_input = raw_inputs[i]
        try:
            json_str = json.dumps(current_input)
            if len(json_str) > 100:
                raise ValueError("Input too large")
            validate_game_input(current_input)
            if current_input["type"] == "score":
                total_score += current_input["value"]
            processed_count += 1
            print(f"Processed valid input: {current_input}")
        except (ValueError, TypeError) as e:
            print(f"Validation failed: {str(e)} for input {current_input}")
        i += 1
    print(f"Loop finished. Processed: {processed_count}, Total score: {total_score}")
if __name__ == "__main__":
    main_processing_loop()