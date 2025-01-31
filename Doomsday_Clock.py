#!/usr/bin/python3
# coding: utf-8

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, QDateTime

class TimeDisplay(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setStyleSheet("font-size: 24pt;")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(60000)  # 1分ごとに更新

        self.updateTime()

        self.setWindowTitle('終末時計')
        self.show()

    def updateTime(self):
        current_time = QDateTime.currentDateTime()
        target_time = QDateTime(2025, 7, 5, 4, 18)
        remaining_time = current_time.secsTo(target_time)
        if remaining_time <= 0:
            self.label.setText("時間が経過しました。アプリケーションを終了します。")
            QTimer.singleShot(3000, self.close)  # 3秒後にアプリケーションを終了
        else:
            minutes_remaining = remaining_time // 60
            self.label.setText(f"終末まで {minutes_remaining} 分")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimeDisplay()
    sys.exit(app.exec_())
