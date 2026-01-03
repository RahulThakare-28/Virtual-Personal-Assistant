from core.event_bus import event_bus

def handle_multimodal(data):
    if data.confidence < 0.6:
        event_bus.emit("ASK_CONFIRMATION", data)
    else:
        event_bus.emit("SEND_TO_BRAIN", data)

event_bus.subscribe("MULTIMODAL_READY", handle_multimodal)
