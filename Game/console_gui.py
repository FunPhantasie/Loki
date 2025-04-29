# cmd_style_console.py

import sys, os, getpass
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QFont, QColor, QPalette, QTextCursor,QIcon

class CmdLikeTextEdit(QTextEdit):
    def __init__(self, parent, prompt_callback):
        super().__init__(parent)
        self.prompt_callback = prompt_callback
        self.prompt = self.prompt_callback()
        self.append(self.prompt)
        self.command = ""

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Backspace, Qt.Key_Left):
            if self.textCursor().positionInBlock() <= len(self.prompt):
                return  # Prevent deleting prompt
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            line = self.toPlainText().splitlines()[-1]
            cmd = line[len(self.prompt):].strip()
            self.parent().process_command(cmd)
            self.append("")  # Move to next line
            self.prompt = self.prompt_callback()
            self.append(self.prompt)
            return
        super().keyPressEvent(event)

class ConsoleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Command Prompt")
        self.setWindowIcon(QIcon("assets/cmd.ico"))
        layout = QVBoxLayout(self)

        self.console = CmdLikeTextEdit(self, self.get_prompt)
        layout.addWidget(self.console)

        self.apply_cmd_style(self.console)

        # Startup text
        self.console.append("Microsoft Windows [Version 10.0.19045.2965]")
        self.console.append("(c) Microsoft Corporation. All rights reserved.\n")
        self.console.append(self.console.prompt)

        # Music player
        self.player = QMediaPlayer()
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        music_path = os.path.join(base_path, "assets", "Outro.m4a")
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(music_path)))

    def apply_cmd_style(self, widget):
        font = QFont("Lucida Console", 10)
        palette = QPalette()
        #palette.setColor(QPalette.Base, QColor(30, 30, 30))  # CMD gray-black
        #palette.setColor(QPalette.Text, QColor(255, 255, 255))  # White text
        palette.setColor(QPalette.Window, QColor(30, 30, 30))  # Window background
        palette.setColor(QPalette.WindowText, Qt.white)  # Title text
        palette.setColor(QPalette.Base, QColor(30, 30, 30))  # Text area
        palette.setColor(QPalette.AlternateBase, QColor(45, 45, 45))
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(45, 45, 45))  # Button bg
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.Highlight, QColor(90, 90, 90))
        palette.setColor(QPalette.HighlightedText, Qt.white)

        widget.setFont(font)
        widget.setPalette(palette)
        widget.setStyleSheet("border: none; background-color: #1e1e1e; color: white;")

    def get_prompt(self):
        username = getpass.getuser()
        return f"C:\\Users\\{username}>"

    def process_command(self, cmd):
        if cmd == "play music":
            self.console.append("🎵 Playing music...\n")
            self.player.play()
        elif cmd == "help":
            self.console.append("Available commands:\n  play music\n  help\n")
        elif cmd == "clear":
            self.console.clear()
            self.console.append("Microsoft Windows [Version 10.0.19045.2965]")
            self.console.append("(c) Microsoft Corporation. All rights reserved.\n")
        else:
            self.console.append(f"'{cmd}' is not recognized as an internal or external command.\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ConsoleApp()
    win.resize(800, 500)
    win.show()
    sys.exit(app.exec_())
