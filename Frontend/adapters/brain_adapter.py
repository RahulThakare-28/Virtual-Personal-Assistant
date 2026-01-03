from core.event_bus import event_bus

def send_to_backend(data):
    print("Sending to backend:", data)

event_bus.subscribe("SEND_TO_BRAIN", send_to_backend)
