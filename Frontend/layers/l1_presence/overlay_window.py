from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QColor

from Frontend.core.event_bus import event_bus


class OverlayWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(80, 80)
        self.drag_pos = QPoint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 180, 255, 200))  # visible blue
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, 80, 80)

    def mousePressEvent(self, event):
        self.drag_pos = event.globalPosition().toPoint()
        event_bus.emit("ACTIVATE_INPUT")

    def mouseMoveEvent(self, event):
        delta = event.globalPosition().toPoint() - self.drag_pos
        self.move(self.pos() + delta)
        self.drag_pos = event.globalPosition().toPoint()
