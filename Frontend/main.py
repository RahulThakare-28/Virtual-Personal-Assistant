from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
import sys

from layers.l1_presence.overlay_window import OverlayWindow
from layers.l2_multimodal.voice_input import simulate_voice

#simulate_voice("close this")

app = QApplication(sys.argv)

window = OverlayWindow()
window.move(300, 300)   # force visible position
window.show()

w = QWidget()
w.setWindowTitle("R3 Frontend Test")
w.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
w.setAttribute(Qt.WA_TranslucentBackground)
w.resize(120, 120)

sys.exit(app.exec())


