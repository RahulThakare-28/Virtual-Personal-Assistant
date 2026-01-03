from core.event_bus import event_bus
from core.data_models import MultimodalInput
from .cursor_tracker import get_cursor
from .screen_context import get_active_app
from .temporal_binder import binder

def on_voice_input(data):
    binder.add_voice(data)

    fused = MultimodalInput(
        text=data["text"],
        cursor_position=get_cursor(),
        active_app=get_active_app(),
        confidence=data["confidence"]
    )

    event_bus.emit("MULTIMODAL_READY", fused)

event_bus.subscribe("VOICE_INPUT", on_voice_input)
