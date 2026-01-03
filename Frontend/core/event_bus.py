class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, callback):
        self.subscribers.setdefault(event, []).append(callback)

    def emit(self, event, data=None):
        for callback in self.subscribers.get(event, []):
            callback(data)

event_bus = EventBus()
