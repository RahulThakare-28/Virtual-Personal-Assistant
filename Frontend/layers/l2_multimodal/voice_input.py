import time
from core.event_bus import event_bus

def on_activate(_):
    payload = {
        "text": "close this",
        "timestamp": time.time(),
        "confidence": 0.85
    }
    print("Voice simulated:", payload)
    event_bus.emit("VOICE_INPUT", payload)

event_bus.subscribe("ACTIVATE_INPUT", on_activate)
