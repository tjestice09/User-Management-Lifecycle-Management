import json
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

def log_access_event(user_event, filename="access_log.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    
    data.append(user_event)
    
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

        
    