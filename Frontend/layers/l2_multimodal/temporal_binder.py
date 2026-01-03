from collections import deque
import time

BUFFER_TIME = 5  # seconds

class TemporalBinder:
    def __init__(self):
        self.voice_buffer = deque()

    def add_voice(self, data):
        self.voice_buffer.append(data)
        self.cleanup()

    def cleanup(self):
        now = time.time()
        while self.voice_buffer and now - self.voice_buffer[0]["timestamp"] > BUFFER_TIME:
            self.voice_buffer.popleft()

    def latest_voice(self):
        return self.voice_buffer[-1] if self.voice_buffer else None

binder = TemporalBinder()
