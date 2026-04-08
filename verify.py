import hashlib
import json

def hash_event(event):
    content = f"{event['event_id']}{event['timestamp']}{event['input_hash']}{event['output_hash']}{event['previous_hash']}"
    return hashlib.sha256(content.encode()).hexdigest()

def verify_chain(ledger):
    for i, event in enumerate(ledger):
        calculated = hash_event(event)
        if calculated != event["event_hash"]:
            print(f"Error in event {event['event_id']}")
            return False
        if i > 0 and event["previous_hash"] != ledger[i-1]["event_hash"]:
            print("Chain broken")
            return False
    return True

with open("ledger.json") as f:
    ledger = json.load(f)

if verify_chain(ledger):
    print("Ledger is valid")
else:
    print("Ledger is compromised")
